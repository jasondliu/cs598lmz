import ctypes
# Test ctypes.CField()

import os
from ctypes import *

if sizeof(c_long) == sizeof(c_void_p):
    c_ssize_t = c_long
else:
    c_ssize_t = c_int

class statvfs_t(Structure):
    _fields_ = [
        ('f_bsize', c_ulong),
        ('f_frsize', c_ulong),
        ('f_blocks', c_fsblkcnt_t),
        ('f_bfree', c_fsblkcnt_t),
        ('f_bavail', c_fsblkcnt_t),
        ('f_files', c_fsfilcnt_t),
        ('f_ffree', c_fsfilcnt_t),
        ('f_favail', c_fsfilcnt_t),
        ('f_fsid', c_ulong),
        ('f_flag', c_ulong),
        ('f_namemax', c_ulong),
    ]
    _fields_ = [
