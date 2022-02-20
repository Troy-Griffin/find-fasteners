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

The chosen solution to this problem was to train a model to recognise fastener types using transfer learning based on the ResNet-18 CNN (Convolutional Neural Network). The size of objects was then found using Aruco Markers to determine the pixel to mm ratio for the image and relating this ratio to the amount of pixels occupied by each object. <br> <br>

It is important to note that the camera should be mounted vertically above the area where samples are analysed to avoid the error of parallax and the camera should be kept at a fixed distance from the analyzation area to provide consistent results.

# 3. Aruco Markers

Aruco Markers are special symbols which are usually used for pose estimation and camera calibration. They are robust and efficient as the camera can locate and analyze them with relative ease. <br> <br>

More information regarding Aruco Markers and their various applications can be found [here](https://docs.opencv.org/4.x/d9/d6d/tutorial_table_of_content_aruco.html)

# 4. Project Requirements

The Hardware and Software requirements to complete this project can be found below: <br> <br>
## Hardware:<br>
* [NVIDIA Jetson Nano Developer Kit, 2GB or 4GB](https://developer.nvidia.com/embedded/jetson-nano-developer-kit)
* [7inch HDMI LCD Display, IMX219-77 Camera, Micro SD Card 64GB or More](https://www.amazon.com/Developer-Accessories-Powerful-Development-XYGStudy/dp/B08629Y5JR/ref=sr_1_1_sspa?dchild=1&keywords=nvidia%2Bjetson%2Bnano%2Bdisplay&qid=1606178640&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzTkZDV1A2REZGVVhPJmVuY3J5cHRlZElkPUExMDM4NDgyMkdTS1dWSkNXWks0WSZlbmNyeXB0ZWRBZElkPUEwMzk0NjI2MzlVVUlZUzVFQkxVUCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1)
* [AC8265 Wireless NIC Module](https://www.amazon.com/Wireless-AC8265-Wireless-Developer-Support-Bluetooth/dp/B07V9B5C6M/ref=pd_day0fbt_img_1/130-9141069-3820329?pd_rd_w=Icn1h&pf_rd_p=bcb8482a-3db5-4b0b-9f15-b86e24acdb00&pf_rd_r=A4ZYHQHC7F6DSBTK2D52&pd_rd_r=7c30cc4d-383b-432a-8a7f-1a4192f57d70&pd_rd_wg=uGeVN&pd_rd_i=B07V9B5C6M&psc=1)
* [5V Power Supply](https://www.amazon.com/gp/product/B07TYQRXTK/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1)<br> <br>
For a comprehensive list of other supported cameras click [here](https://developer.nvidia.com/embedded/jetson-partner-supported-cameras?t1_max-resolution=4K)<br> <br>
The Jetson Nano can also be powered by a 5V power supply with a Barrel Jack connnector.

## Software:<br>
* Latest version of NVIDIA Jetpack. The steps to set this up on your Jetson Nano can be found in section [5.1. Jetpack](#51-jetpack).

# 5. Setup

The general setup of the Jetson Nano developer kit is covered [here](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit)

## 5.1. Jetpack

The latest version of Jetpack can be downloaded by following these [steps](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#write)

## 5.2. Camera

Depending on the type of camera you are using you will need to comment out diffrent sections of the code.<br> <br>

If you are using a Webcam comment out the folowing line:<br>
` edit <br> <br>

If you are using a CSI camera comment out the following line:<br>
` edit

## 5.3. Required Packages



# 6. Modifications



# 7. Run the Script


