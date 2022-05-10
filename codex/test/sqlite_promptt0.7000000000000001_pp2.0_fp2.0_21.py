import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")
import sys
import xml.etree.ElementTree as ET
import pdb
import subprocess
import time
import os
import datetime
import re
import tempfile

reload(sys)
sys.setdefaultencoding('utf8')

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def is_numeric(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_ascii_numeric(s):
    return all(ord(c) < 128 and (ord(c) >= 48 and ord(c) <= 57) for c in s)

def is_ascii_alpha(s):
    return all(ord(c) < 128 and (ord(c) >= 65 and ord(c) <= 90 or ord(c) >= 97 and ord(c) <= 122) for c in s)

