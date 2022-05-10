import ctypes
# Test ctypes.CField behavior:
# 1. Read a long, combine with a short, store in a long
# 2. Read 2 longs, shift the first one left, store it in a long long
# 3. Read a long long, and a long, shift the long long right, store in a
#    long long.

import struct
from struct import *

import ctypes
import ctypes.wintypes as wintypes
from ctypes.wintypes import *

def to_bytes(n, length, order="big"):
    h = "%%0%ix" % (length * 2)
    s = h % n
    s = s.encode("ascii")
    s = bytes.fromhex(s)
    return s

class MyStructure(ctypes.Structure):
    _fields_ = [
        ("a", wintypes.DWORD),
        ("b", ctypes.c_ushort),
        ("c", wintypes.DWORD),
        ("d", wintypes.DWORD),
        ("e", wintypes.DWORD),
        ("f
