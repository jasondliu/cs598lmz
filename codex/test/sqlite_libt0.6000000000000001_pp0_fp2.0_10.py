import ctypes
import ctypes.util
import threading
import sqlite3

from . import _v4l2
from . import _common
from . import _v4l2_device
from . import _v4l2_ioctl


_libc_path = ctypes.util.find_library("c")
_libc = ctypes.CDLL(_libc_path, use_errno=True)

_libv4l2_path = ctypes.util.find_library("v4l2")
_libv4l2 = ctypes.CDLL(_libv4l2_path, use_errno=True)


def _extract_errno(fn):
    if hasattr(fn, "_errno"):
        errno = ctypes.get_errno()
        if errno != 0:
            raise OSError(errno, os.strerror(errno))
    return fn


def _extract_errno_retval(fn):
    if hasattr(fn, "_errno"):
        errno = ctypes.get_errno()
