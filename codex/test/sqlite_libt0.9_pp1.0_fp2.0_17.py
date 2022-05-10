import ctypes
import ctypes.util
import threading
import sqlite3 as sqlite
import binascii
import sys
import traceback

from config import DEPs, DEBUGDEP

import ctypes
import ctypes.util

libm = ctypes.CDLL(ctypes.util.find_library('m'), use_errno=True)

log = logging.getLogger("pylogger")

def enum(**enums):
  return type('Enum', (), enums)

#Not so clean. Error codes taken from https://code.google.com/p/chromium/codesearch#chromium/src/base/third_party/dmg_fp/dtoa.h
ERRNO_CODES = enum(
    RESULT_INEXACT     = -1,
    RESULT_UNDERFLOW   = -2,
    RESULT_OVERFLOW    = -3,
    RESULT_FATAL       = -4,
    RESULT_FAILURE     = -5,
    RESULT_SUCCESS     = -6
)

