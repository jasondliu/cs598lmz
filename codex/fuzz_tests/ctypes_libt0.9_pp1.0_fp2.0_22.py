import ctypes
ctypes.cdll.LoadLibrary('/usr/lib/libboost_python.so')
import rospy
from std_msgs.msg import String
import os
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy
import sys
sys.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages')
import tensorflow as tf
import json
import sys
sys.path.append('./Tenso')
import cv2
import PIL.Image as Image
import PIL.ImageColor as ImageColor
import PIL.ImageDraw as ImageDraw
import PIL.ImageFont as ImageFont
import random
import time
import math

cameraID=sys.argv[1]
print(cameraID)

#os.environ['CUDA_VISIBLE_DEVICES']='1'
PATH_TO_CKPT = './Tenso/trained-inference-graphs/output_inference_graph.pb'
PATH_TO_LABELS = './
