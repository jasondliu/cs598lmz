import mmap
# Test mmap.mmap(0, 0) on Windows
# This is a temporary workaround for http://bugs.python.org/issue8776
m = mmap.mmap(0, 0)
m.close()
del m
import os, sys, platform, struct
from struct import calcsize, unpack, pack
from sys import byteorder, exc_info
from datetime import datetime, date, timedelta
from .util import *
from .json import JSONFile
from .config import Config
from . import fs
from . import crypto
from . import block

FMT_VERSION = 1
FMT_BLOCKLEN = 16 # AES block length in bytes

def read_meta(f):
    # read the metadata format version
    fmtver = int(f.readline())
    if fmtver != FMT_VERSION:
        raise Error('Unknown metadata format version: %d' % fmtver)
    
    # read the metadata json
