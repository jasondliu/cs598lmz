import ctypes
import ctypes.util
import threading
import sqlite3
import logging
import time
import os
import sys
import errno
import re
import random
import hashlib
import binascii
import traceback
import subprocess
import platform
import json

from . import constants
from . import util

log = logging.getLogger(__name__)

# These are not available in the global namespace
# because we want to avoid importing them unless
# they are actually used.
_libc = None
_libc_name = None
_libc_version = None
_libc_version_info = None

def _get_libc():
    global _libc
    global _libc_name
    global _libc_version
    global _libc_version_info
    if _libc is not None:
        return _libc
    libc_name = ctypes.util.find_library('c')
    if libc_name is None:
        raise ImportError('libc not found')
    _libc_name = libc_name
    _libc = ctypes.CDLL(libc_name
