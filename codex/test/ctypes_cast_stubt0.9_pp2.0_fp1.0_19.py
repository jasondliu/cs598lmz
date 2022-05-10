import ctypes
ctypes.cast(1, ctypes.py_object)

import decimal
decimal.Decimal(1)
hex(id(decimal.Decimal(1)))

import string
string.ascii_letters

import sys
sys.path

import warnings
warnings.warn("CT")
warnings.warn("PC")

import zlib
zlib.crc32(b"test")

import io
io.StringIO("test")

import lzma
lzma.LZMAFile

import time
time.gmtime(1234567890)

import _testcapi
