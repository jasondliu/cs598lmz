import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import hashlib
import logging
import base64
import binascii
import json
import uuid
import re

from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Util import Counter

from . import config

logger = logging.getLogger(__name__)

#
# Utility functions
#

def get_library_path():
    if sys.platform == "darwin":
        return ctypes.util.find_library("libanaconda.dylib")
    else:
        return ctypes.util.find_library("libanaconda")

def get_library():
    library_path = get_library_path()
    if library_path:
        return ctypes.cdll.LoadLibrary(library_path)
    else:
        logger.error("No library found.")
        return None

def get_library_version():
    library = get_library()
    if not library:
        return None

    return library.anaconda_version()

