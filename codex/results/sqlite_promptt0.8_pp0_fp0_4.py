import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file::memory:?cache=shared', uri=True)
# To share the connection between threads.
import memcache
from time import time
from collections import namedtuple
from ctypes import byref
from ctypes.wintypes import (
    BOOL, BYTE, DWORD, HANDLE, LPCWSTR, LPVOID, LPWSTR, UINT
)
from win32con import (
    ERROR_INSUFFICIENT_BUFFER, ERROR_NOT_SUPPORTED, ERROR_SUCCESS,
    ERROR_TOO_MANY_CMDS, ERROR_TOO_MANY_SESS, ERROR_TOO_MANY_SEM_REQUESTS,
    ERROR_TOO_MANY_SEMAPHORES, ERROR_TOO_MANY_TCBS, GENERIC_READ,
    GENERIC_WRITE, OPEN_ALWAYS, OPEN_EXISTING, PROCESS_ALL_ACCESS,
    PROCESS_QUERY_INFORMATION, PROCESS_TERMINATE, READ_CONTROL, STANDARD_RIGHTS_READ
