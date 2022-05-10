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
