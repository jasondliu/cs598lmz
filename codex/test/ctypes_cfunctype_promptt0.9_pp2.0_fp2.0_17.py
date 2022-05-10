import ctypes
# Test ctypes.CFUNCTYPE and C backend

import ctypes
import _ctypes
from ctypes import _endian
import unittest, sys

LittleEndianStructure = None
BigEndianStructure = None

# For now, we only support LE and BE

