import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
import logging
import json
import sys
import time
import random
import re
import pprint

# if ctypes.sizeof(ctypes.c_void_p) == 8:
#     lib = ctypes.CDLL(ctypes.util.find_library("libcgroup"))
# else:
#     lib = ctypes.CDLL(ctypes.util.find_library("cgroup"))
#
# if lib.cgroup_init() != 0:
#     raise RuntimeError("cgroup_init() failed")
#
# cgroup_destroy = lib.cgroup_destroy
# cgroup_destroy.argtypes = [ctypes.c_void_p]
# cgroup_destroy.restype = None
#
# def destroy(cgroup):
#     cgroup_destroy(cgroup)
#
# cgroup_get_cgroup = lib.cgroup_get_cgroup
# cgroup_get_cgroup.argtypes = [ctypes.c_void_p]
# cgroup_get_cgroup.restype = ctypes.c_void
