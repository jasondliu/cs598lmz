import mmap
# Test mmap.mmap()
import os
# Test os.ftruncate()
import random
# Test random.random()
import re
# Test re.compile()
import shutil
# Test shutil.rmtree()
import socket
# Test socket.socket()
import subprocess
# Test subprocess.Popen()
import sys
# Test sys.stdout
import threading
# Test threading.Thread()
import time
# Test time.sleep()
import traceback
# Test traceback.format_stack()
import unittest
# Test unittest.TestCase()
import urllib
# Test urllib.urlopen()
import xmlrpclib
# Test xmlrpclib.ServerProxy()
import zipfile
# Test zipfile.ZipFile()

# We only need to test these modules if we are on Windows
if sys.platform == 'win32':
    import _winreg
    # Test _winreg.OpenKey()
    import pywintypes
    # Test pywintypes.error
    import win32api
    # Test win32api.GetUser
