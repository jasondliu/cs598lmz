import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect, only SQLite available in Python 2.6
import sqlite3 as dbh

# Test ifctypes
import ifc
# Test cfx for RotoScope
try:
  import cfx
except:
  cfx = False
# Test FFMPEG
import mpeg.api
# Test PIL
import PIL
# Test JDK
import javax.swing
# Test Blackmagic Desktop Video, before we test it with SDK
try:
  import bmd
except:
  bmd = False
# Test ImgQuant
import imgquant

# Test COM
try:
  import win32com
except:
  win32com = False

# Test pycrypto
import Crypto
import Crypto.Util.number

# Test PyYAML
import yaml

# Test the engine bridge
import natron_bridge

# Test PyQt4 before Qt.py
try:
  import PyQt4
except:
  PyQt4 = False

# Test Qt.py
import Qt as qt

# Test PySide
