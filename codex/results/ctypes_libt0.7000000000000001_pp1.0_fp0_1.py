import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

import wx
import wx.lib.newevent
import wx.lib.agw.customtreectrl

import gc

import time
import threading
import multiprocessing

import sys
import os
import io
import traceback
import random

import numpy as np

import config

import cv2
import img_tools

import copy

import json
import pickle

import scipy.misc

import KMeans

import wx_tools
import wx_panels

###

import matplotlib
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure

###


#
#
#

#
#
#

#
#
#

class DataThread(threading.Thread):
	def __init__(self,func,*args,**kwargs):
		threading.
