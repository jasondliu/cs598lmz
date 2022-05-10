import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import weakref

if sys.platform.startswith("win"):
    import win32api
    import pywintypes
    win32api.LoadLibrary("shlwapi.dll")

__all__ = [
    "DB_INIT_MPOOL", "DB_INIT_CDB", "DB_INIT_LOCK", "DB_INIT_LOG",
    "DB_INIT_TXN", "DB_DIRECT_DB", "DB_RECOVER", "DB_CREATE", "DB_THREAD",
    "DB_REGISTER", "DB_RECOVER_FATAL", "DB_INIT_REP", "DB_ENV_XA_CREATE",
    "DB_ENV_XA_ERR_NOTA", "DB_ENV_XA_ERR_INVAL", "DB_ENV_XA_ERR_PROTO",
    "DB_ENV_XA_ERR_RMERR", "DB_ENV_XA_RETRY", "DB_ENV
