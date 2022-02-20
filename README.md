# find-fasteners
An identifier of bolt and nut (fastener) types aswell as sizes. NVIDIA AI Specialist Certification Project. Nvidia Jetson Nano.
## Contents
1. [Motivation](#1-motivation)
2. [Solution Summary](#2-solution-summary)
3. [Aruco Markers](#3-aruco-markers)
4. [Project Requirements](#4-project-requirements)
5. [Setup](#5-setup)<br>
  5.1. [Jetpack](#51-jetpack)<br>
  5.2. [Camera](#52-camera)<br>
  5.3. [Required Packages](#53-required-packages)<br>
6. [Modifications](#6-modifications)
7. [Run the Script](#7-run-the-script)
<hr>

# 1. Motivation

Home and Commercial projects often come to an end with surplus fasteners (Nuts, Bolts, Screws, etc..) in inventory. More often than not, particularly in a home enviroment, surplus fasteners are stored together in what becomes a large accumulation of assorted fasteners. It can be difficult to make use of these fasteners as they accumulate and become disorganised. The aim of this project is to provide the framework of a solution which can be coupled with mechanical actuation to automate the process of sorting fasteners by type and size.

# 2. Solution Summary

The solution to this problem was to train a model to recognise fastener types using transfer learning based on the ResNet-18 CNN (Convolutional Neural Network). The size of objects was found using Aruco Markers to determine the pixel to mm ratio and then relate this to the amount of pixels occupied by each object. <br> <br>
It is important to note that the camera should be mounted vertically above the area where samples are analysed to avoid the error of parallax and the camera should be kept at a fixed distance from the analyzation area to provide consistent results.

# 3. Aruco Markers

Aruco Markers are special symbols which are usually used for pose estimation and camera calibration. They are robust and efficient as the camera can locate and analyze them with relative ease. <br> <br>
More can be read about Aruco Markers and their various applications [here](https://docs.opencv.org/4.x/d9/d6d/tutorial_table_of_content_aruco.html)

# 4. Project Requirements



# 5. Setup



## 5.1. Jetpack



## 5.2. Camera



## 5.3. Required Packages



# 6. Modifications



# 7. Run the Script


