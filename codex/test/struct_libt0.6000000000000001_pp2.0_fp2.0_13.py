import _struct
import _vmprof
import _weakref
import array
import asc
import binascii
import cmath
import ctypes
import gc
import itertools
import marshal
import math
import mmap
import operator
import parser
import pyexpat
import re
import signal
import socket
import struct
import sys
import time
import unicodedata
import zlib

# create a simple class to get a C-level object, so that we can
# test the tp_clear slot
class X(object):
    pass

class Y(object):
    pass

def test_clear():
    x = X()
    y = Y()
    x.a = y
    x.b = y
    x.c = y
    x.d = y
    x.e = y
    x.f = y
    x.g = y
    x.h = y
    # should not crash
    del y
    gc.collect()

def test_del_slot():
    class X(object):
        pass
    x = X()
    x
