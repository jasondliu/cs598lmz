import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys

# ctypes stuff

# Not sure if we'll need these
# libc = ctypes.CDLL(ctypes.util.find_library('c'))
# libc.setuid.argtypes = [ctypes.c_uint32]
# libc.setuid.restype = ctypes.c_int
# libc.setgid.argtypes = [ctypes.c_uint32]
# libc.setgid.restype = ctypes.c_int

libcgroup = ctypes.CDLL(ctypes.util.find_library('cgroup'))
libcgroup.cgroup_get_current_controller_path.argtypes = [ctypes.c_char_p]
libcgroup.cgroup_get_current_controller_path.restype = ctypes.c_int
libcgroup.cgroup_get_current_controller_path.restype = ctypes.c_int
libcgroup.cgroup_get_current_controller_path.restype = ctypes.c_int

# This is
