import ctypes
import ctypes.util
import threading
import sqlite3

# only used for alpm_list_t
class alpm_list(ctypes.Structure):
    _fields_ = [
        ("prev", ctypes.c_void_p),
        ("next", ctypes.c_void_p),
        ("data", ctypes.c_char_p)
    ]

import alpm

buffer = ctypes.create_string_buffer(65536)

alpm.alpm_initialize()
alpm.alpm_set_option(alpm.PM_OPT_LOGMASK, alpm.PM_LOG_DEBUG)
handle = alpm.alpm_initialize()
assert handle != None

handle = alpm.alpm_initialize()
assert handle != None

for line in file("/var/lib/pacman/" + os.getenv("DB") + "/repos"):
    if line[0:1] == "#":
        continue

    depth = 0
    for c in line:
        if c == "[":
            depth += 1
