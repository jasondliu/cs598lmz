import ctypes
import ctypes.util
import threading
import sqlite3

from . import jsonrpc


# Some constants
#
# These are taken from the libc headers
# Note: We just need the constants and not the whole library.
#       This saves us a dependency to libc
LIBC = ctypes.cdll.LoadLibrary(ctypes.util.find_library('c'))

SIG_DFL = ctypes.c_int.in_dll(LIBC, 'SIG_DFL').value
SIG_IGN = ctypes.c_int.in_dll(LIBC, 'SIG_IGN').value
SIGCHLD = ctypes.c_int.in_dll(LIBC, 'SIGCHLD').value

SIGHUP = ctypes.c_int.in_dll(LIBC, 'SIGHUP').value
SIGINT = ctypes.c_int.in_dll(LIBC, 'SIGINT').value
SIGQUIT = ctypes.c_int.in_dll(LIBC, 'SIGQUIT').value
