import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import string
import time
import re
import socket
import struct
import hashlib
import logging
import logging.handlers
import traceback
import datetime
import shutil
import subprocess
import signal
import getopt
import random
import tempfile
import base64
import binascii

#------------------------------------------------------------------------------

#
# Logging
#

def getLogger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger

#------------------------------------------------------------------------------

#
# Constants
#

MAX_PATH = 260

#
# Windows API
#

class FILETIME(ctypes.Structure):
    _fields_ = [
       
