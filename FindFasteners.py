import cv2
import jetson.inference
import jetson.utils
import numpy as np

width = 1280
height = 960
dispW = width
dispH = height

flip = 2
camSet = 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam = cv2.VideoCapture(camSet)
# cam=cv2.VideoCapture(1)

cam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)

net1 = jetson.inference.imageNet(argv=['--model=/home/troy/find-fasteners/models/NutType/resnet18.onnx', '--input_blob=input_0', '--output_blob=output_0', '--labels=/home/troy/find-fasteners/models/NutType/labels.txt'])
net2 = jetson.inference.detectNet(argv=['--model=/home/troy/find-fasteners/models/findFastenerObjects/ssd-mobilenet.onnx', '--labels=/home/troy/find-fasteners/models/findFastenerObjects//labels.txt', '--input-blob=input_0', '--output-cvg=scores', '--output-bbox=boxes'])
font = cv2.FONT_HERSHEY_PLAIN

while True:
    _, frame = cam.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA).astype(np.float32)
    img = jetson.utils.cudaFromNumpy(img)

    aruco = cv2.aruco.DetectorParameters_create()
    aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)
    arucoCorners, _, _ = cv2.aruco.detectMarkers(frame, aruco_dict, parameters=aruco)
    if arucoCorners:
        arucoShape = np.intp(arucoCorners)
        cv2.polylines(frame, arucoShape, True, (0, 0, 255), 4)
        arucoPerimeter = cv2.arcLength(arucoCorners[0], True)
        pixel_mm_ratio = arucoPerimeter / 200

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        mask = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 19, 5)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
    detections = net2.Detect(img, width, height)
    for detect in detections:
        if detect != []:
            try:
                ID = detect.ClassID
                item = net2.GetClassDesc(ID)
                confidence = detect.Confidence

                if item == 'Nut':
                    # Generate ROI
                    roi = frame[int(detect.Left)-50:int(detect.Right), int(detect.Top):int(detect.Bottom)+50]
                    height1 = roi.shape[0]
                    width1 = roi.shape[1]
                    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGBA).astype(np.float32)
                    roi = jetson.utils.cudaFromNumpy(roi)

                    # Image Classification
                    classID, confidence = net1.Classify(roi, width1, height1)
                    item = net1.GetClassDesc(classID)
                    
                cv2.putText(frame, str(item) + ' ' + str(round(confidence, 2)), ((int(detect.Left)), (int(detect.Top))), font, 1, (0, 255, 0), 2)
            except:
                pass
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    mask = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 19, 5)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        try:
            rectangle = cv2.minAreaRect(cnt)
            (x, y), (w, L), angle = rectangle
            area = cv2.contourArea(cnt)
            if area > 2500:
                border = cv2.boxPoints(rectangle)
                border = np.intp(border)
                cv2.polylines(frame, [border], True, (0, 255, 0), 3)

                oWidth = w / pixel_mm_ratio
                oLength = L / pixel_mm_ratio

                cv2.putText(frame, "Width {}mm".format(round(oWidth, 1)), ((int(x-50)), (int(y-30))), font, 1, (0, 255, 0), 2)
                cv2.putText(frame, "Length {}mm".format(round(oLength, 1)), ((int(x-50)), (int(y+30))), font, 1, (0, 255, 0), 2)
        except:
            pass

    cv2.imshow('findFasteners', frame)
    cv2.moveWindow('findFasteners', 0, 0)

    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
