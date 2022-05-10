import ctypes
import ctypes.util
import threading
import sqlite3
import json
import sys
import os

from . import _librsync
from . import _librsync_c

_librsync_c.rs_trace_set_level(_librsync_c.RS_LOG_DEBUG)

class RsyncError(Exception):
    pass

class RsyncPatchError(RsyncError):
    pass

class RsyncSignatureError(RsyncError):
    pass

class RsyncDeltaError(RsyncError):
    pass

class RsyncFileDeltaError(RsyncError):
    pass

def _trace(typ, message):
    print(message.decode('utf-8'))

#_librsync_c.rs_trace_set_level(_librsync_c.RS_LOG_DEBUG)
#_librsync_c.rs_trace_set_callback(_trace)

def _check_error(err):
    if err < 0:
        raise RsyncError(_librsync_c.rs_strerror(err))

def _check_error_free(err, ptr
