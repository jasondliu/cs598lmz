import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys
import hashlib
import inspect

# First resolve all functions in the C library.

# PyRun_SimpleFile is not available on older Pythons.  It is available
# on Python 2.2 and newer.  PyRun_SimpleString() should be slightly
# faster than PyRun_File().
#
# Begin PyRun_SimpleString.
def PyRun_SimpleString(statement):
	g = {}
	l = {}
	exec statement in g, l
# End PyRun_SimpleString.

mkdtemp = ctypes.cdll.msvcrt.mkdtemp
PathRemoveFileSpec = ctypes.cdll.shlwapi.PathRemoveFileSpecA
PathIsFileSpec = ctypes.cdll.shlwapi.PathIsFileSpecA
PathAddBackslash = ctypes.cdll.shlwapi.PathAddBackslashA
PathAppend = ctypes.cdll.shlwapi.PathAppendA
GetFileAttributes = ctypes.cdll.kernel32.GetFileAttributesA
CreateFile =
