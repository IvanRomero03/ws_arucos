import rospy
import cv2
import numpy
from sensor_msgs.msg import Image, CameraInfo
from cv_bridge import CvBridge, CvBridgeError
from detector_arucos.msg import objectDetection, objectDetectionArray
from geometry_msgs.msg import Point, Quaternion
import os
import sys

IMAGE_TOPIC = "/image"

class Detector:
    image = None
    def __init__(self):
        self.node = rospy.Subscriber("")

