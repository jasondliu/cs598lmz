import ctypes
import ctypes.util
import threading
import sqlite3
import logging
from cStringIO import StringIO
from datetime import datetime
from weakref import WeakKeyDictionary
from distutils.spawn import find_executable
from functools import update_wrapper, partial
from .lazy import Lazy, LazyEnum, LazyList, LazyDict
from .compat import dict_iteritems, string_types, long, binary_type
from .utils import strip_c_comments, strip_c_decl, re_matchall, to_u, b


libm = None
libz = None
librt = None


class LinkMode(LazyEnum):
    HardLink = 1
    SymbolicLink = 2
    File = 3

            
class Link(object):
    __slots__ = ('_id', '_mode', 'path', 'bloom', 'size', 'mtime', 'crc', '_hash')

    def __init__(self, mode, path=None, bloom=None, size=None, mtime=None, crc=None):
        self._mode = mode
