import ctypes
import ctypes.util
import threading
import sqlite3
import os

# This is a simple script to monitor system calls that are made
# by a process. The only argument is the PID of the process to
# monitor. As the process makes system calls, the syscall name,
# and any arguments are printed to stdout.

# This script uses the DTrace syscall provider, and should work
# on any system that supports DTrace.

# This has only been tested on Mac OS X.

dtrace_h = ctypes.CDLL(ctypes.util.find_library('dtrace'), use_errno=True)
libc_h = ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True)

# This is the structure that contains information about a probe.
# It is filled out by the DTrace library, and passed to the
# callback function.
