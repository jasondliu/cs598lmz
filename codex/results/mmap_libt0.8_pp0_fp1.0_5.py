import mmap
import operator
import os
import random
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import traceback
import urllib
import urllib2
import xml.dom.minidom

import wx

SPLASH_IMAGE = "images/splash.png"

BOLD_FONT = None
BOLD_FONT_SIZE = None

def MaybeFormat(message, *args):
	if args:
		return message % args
	return message

def GetBoldFont():
	global BOLD_FONT
	global BOLD_FONT_SIZE

	if not BOLD_FONT:
		if wx.Platform == '__WXMSW__':
			BOLD_FONT = wx.SystemSettings_GetFont(wx.SYS_DEFAULT_GUI_FONT)
			BOLD_FONT.SetWeight(wx.BOLD)
			BOLD_FONT_SIZE = BOLD_FONT.GetPointSize()
			
