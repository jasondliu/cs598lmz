import ctypes
import ctypes.util
import threading
import sqlite3
import random
import time
import sys
import os
import hashlib
import math
import re
import signal
import gtk
import pango
import Queue

from gtk import gdk
import gobject

from PIL import Image
from PIL import ImageChops

# this is a bit of a hack - we should be able to use ctypes.cdll.LoadLibrary
# instead of ctypes.util.find_library, but find_library doesn't work on my
# system (Ubuntu 10.04).  if we can remove this, we won't need to install
# libcurl3-dev (or equivalent) to run
curl = ctypes.cdll.LoadLibrary(ctypes.util.find_library('curl'))

# global variables
#

# curl variables
curl_multi = None
curl_share = None

# the main window
window = None

# the main window's statusbar
statusbar = None

# the main window's notebook
notebook = None

# the main window's search entry
search_entry = None

#
