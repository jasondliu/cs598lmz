import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memdb?mode=memory&cache=shared', uri=True)
import os

libc = ctypes.CDLL(ctypes.util.find_library('c'))

# https://docs.python.org/3/library/ctypes.html#ctypes.CFUNCTYPE
# CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
#   use_errno=False errno attribute of the calling thread is not set.
#   use_last_error=False GetLastError() attribute of the calling thread is not set.

# https://sqlite.org/c3ref/vfs.html
VFS_OPEN = 0
VFS_DELETE = 9
VFS_CHECKRESERVEDLOCK = 18
VFS_FILECONTROL = 22
VFS_SECTORSIZE = 30
VFS_MAXPATHNAME = 31
VFS_SYMLINK = 33
VFS_ACCESS = 34

# https://sqlite.org/c3ref/file_
