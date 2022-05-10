import ctypes
import ctypes.util
import threading
import sqlite3
import time
from collections import OrderedDict

from . import const
from . import util

# libc
DL_OPEN = 2

# dlinfo
RTLD_DI_LINKMAP = 2

# r_debug
RT_CONSISTENT = 0
RT_ADD = 1
RT_DELETE = 2

# dl_phdr_info

# struct link_map
l_addr = 0x00
l_name = 0x08
l_ld = 0x10
l_next = 0x18
l_prev = 0x20

# struct r_debug
r_version = 0x00
r_map = 0x08
r_brk = 0x10
r_state = 0x18
r_ldbase = 0x20


def dlopen(filename, flag):
    libc = ctypes.cdll.LoadLibrary(ctypes.util.find_library("c"))
    return libc.dlopen(filename, flag)


def dlclose(handle):
    libc = ctypes.cdll.
