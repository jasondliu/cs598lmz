import mmap
import os
import sys
import time
import unittest

from ctypes import *
from ctypes.util import find_library

from mock import Mock

import pyuv

libc_name = find_library("c")
if not libc_name:
    raise unittest.SkipTest("libc not found")
libc = CDLL(libc_name)

if sys.platform == 'win32':
    libuv = pyuv.CDLL(pyuv.__file__[:-3] + 'dll')
else:
    libuv = pyuv.CDLL(pyuv.__file__[:-3])

libuv.uv_version.restype = c_uint
libuv.uv_version_string.restype = c_char_p
