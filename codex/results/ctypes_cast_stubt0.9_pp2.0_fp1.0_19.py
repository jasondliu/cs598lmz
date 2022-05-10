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
_testcapi.my_set

#import _randommodule
#_randommodule._r

import selectors
selectors.SelectSelector

import datetime
datetime.datetime(2012, 3, 4, 5)

#import _multibytecodec
#_multibytecodec._multibytecodec

#import _codecs_kr
#_codecs_kr._codecs_kr

import locale
loc
