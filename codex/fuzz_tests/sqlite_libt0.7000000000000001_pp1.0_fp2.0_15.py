import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import math
import time
import datetime
import shutil
import traceback
import subprocess

#gobject.threads_init()

import gobject

#import pygst
#pygst.require("0.10")
import gst

import libavg

# import avglib
# import avglib.glue

import utils

import mediabox_log

import config

logger = mediabox_log.get_logger('mediabox')

gobject.threads_init()

gst.init(None)
libavg.player.enable_vsync(True)

#gst 0.10.19 has a bug which prevents avidemux from working with theora
#if gst.pygst_version >= (0, 10, 19):
#	logger.error("gst version too high (0.10.19)")
#	sys.exit(1)

#gst 0.10.32 has a bug which prevents avidemux from working with mpeg4
