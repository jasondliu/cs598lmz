import ctypes
import ctypes.util
import threading
import sqlite3
import os

from .. import bb

__all__ = [
    'Cache',
    'CacheError',
    'NoDataError',
    'OperationError',
    'ConnectionError',
    'connect',
]


class CacheError(Exception):
    """Generic error class for the librsync module."""


class NoDataError(CacheError):
    """No data in the cache."""


class OperationError(CacheError):
    """Unexpected operation for the cache."""


class ConnectionError(CacheError):
    """General connection error."""


# librsync C type prototypes
rs_job_t = ctypes.c_void_p
rs_buffers_t = ctypes.c_void_p
rs_signature_t = ctypes.c_void_p
rs_result_t = ctypes.c_int

# librsync error codes
RS_DONE = 0
RS_BLOCKED = 1
RS_RUNNING = 2

# librsync signatures
RS_MD4_SIG_MAGIC = 0x727
