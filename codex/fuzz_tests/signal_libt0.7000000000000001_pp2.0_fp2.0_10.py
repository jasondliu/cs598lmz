import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys, os
if len(sys.argv) > 1:
    os.chdir(sys.argv[1])
    del sys.argv[1]

import math

from PyQt5 import QtGui, QtCore, QtNetwork

from gui import gui

#~ from PIL import Image, ImageEnhance


#~ import rosbag
#~ import rospy
#~ import sensor_msgs.point_cloud2 as pc2
#~ from sensor_msgs.msg import PointCloud2, PointField
import numpy as np
#~ from numpy import ma

import pylab

#~ from scipy import ndimage

#~ from sklearn.decomposition import PCA
#~ from sklearn.cluster import KMeans

import time

import matplotlib
matplotlib.rcParams['backend.qt4']='PyQt4'
from matplotlib.backends.backend_qt4agg import
