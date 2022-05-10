import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import os
import datetime
import time
import glob
import re
import subprocess
import shlex
import shutil
import signal
import hashlib
import gzip
import zipfile
import hashlib
import tempfile
import binascii
import xml.dom.minidom
import json
import collections
import functools
import math
import qt
import qt.QtGui
import qt.QtCore
import qt.QtNetwork
import qt.QtWebKit
import qt.QtNetwork

# ------------------------------------------------------------------------------

def get_app_path():
    return os.path.dirname(os.path.abspath(sys.argv[0]))

def get_app_name():
    return os.path.basename(sys.argv[0])

def get_app_version():
    return "1.0"

def get_app_title():
    return "%s %s" % (get_app_name(), get_app_version())

def get_app_icon():
    return
