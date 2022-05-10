import ctypes
# Test ctypes.CFUNCTYPE()

from ctypes import *
from ctypes import wintypes

import unittest

# for dumping the function prototype
import sys

from sys import platform
if platform == "darwin":
    from ctypes import objc

# for sizeof
import struct

# for isinstance(x, integer_types)
