import _struct
from helpers import *
from config import *

from PIL import Image

import base64
from StringIO import StringIO


from PIL import Image
from StringIO import StringIO
from random import randrange

from ctypes import *
import os
import sys
import ctypes
import ctypes.wintypes
import struct

import win32api
import win32gui
import win32ui
import win32con
import win32com.client


##
##
##

user32 = windll.user32

##
##
##

#offset to find the window
GAP_TOP= 5
GAP_LEFT= 5

#offset to find the window
GAP_BOTTOM= 5
GAP_RIGHT= 5

#offset to screen
GAP_SCREEN_TOP= 5
GAP_SCREEN_LEFT= 5

#offset to screen
GAP_SCREEN_BOTTOM= 5
GAP_SCREEN_RIGHT= 5

##
##
##

#'\x1b[38;
