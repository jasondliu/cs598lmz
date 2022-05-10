import ctypes
import ctypes.util
import threading
import sqlite3
import os

from . import util
from . import _librsync
from . import _io


# find the shared library
_lib_path = ctypes.util.find_library("librsync")
if not _lib_path:
    raise RuntimeError("Unable to find librsync shared library")
_librsync_dll = ctypes.cdll.LoadLibrary(_lib_path)


# wrap the shared library
_librsync.wrap_librsync(_librsync_dll)

_lib_version = _librsync_dll.rs_version()

_lib_version_major = (_lib_version >> 16) & 0xffff
_lib_version_minor = _lib_version & 0xffff

if _lib_version_major != 2:
    raise RuntimeError("librsync library version %d.%d not yet supported"
                       % (_lib_version_major, _lib_version_minor))

if _lib_version_minor < 1:
    raise RuntimeError("librsync version 2.0 is not supported")

