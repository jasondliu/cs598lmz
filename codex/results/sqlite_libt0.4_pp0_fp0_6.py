import ctypes
import ctypes.util
import threading
import sqlite3
import os
import re
import sys
import time
import datetime
import subprocess
import json
import shutil
import traceback
import platform
import collections
import random
import logging
import logging.handlers
import urllib.request
import urllib.parse
import urllib.error
import urllib.request
import urllib.error
import urllib.parse
import hashlib
import tempfile
import shutil
import zipfile
import xml.etree.ElementTree as ET
import ssl
import socket
import getpass
import signal
import stat

# check python version
if sys.version_info < (3,0):
    print("Python 3.0 or later is required")
    sys.exit(1)

# check platform
if sys.platform == "win32":
    import ctypes.wintypes
    import msvcrt
    import winreg
    import win32api
    import win32file
    import win32con
    import win32event
    import win32process
    import win32security
    import winerror
    import
