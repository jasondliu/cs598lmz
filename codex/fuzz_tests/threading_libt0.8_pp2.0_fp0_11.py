import threading
threading.currentThread().setName('fetchBilibili')

import sys
import os
import re
import time
import json
import subprocess
import urllib
import urllib2
import urlparse
import cookielib
import ctypes

common = sys.modules["__main__"]

#----------------------------------------------------------------------
def Gmeter2Meter(s):
	"""
	Gram to meter
	"""
	pat = re.compile(r"(\d+\.\d+)G")
	ret = pat.search(s)
	if ret is None:
		return None
	return str(float(ret.group(1))*1000)
#----------------------------------------------------------------------
def GetFileName(s):
	"""
	Get file name from an URL
	"""
	return s[s.rfind("/")+1:]
#----------------------------------------------------------------------
def GetBilibiliVideoInfo(url):
	"""
	Get a dict contain video information from Bilibili
	"""
	if url is None:
		return None
	if url.startswith("http://www.bilib
