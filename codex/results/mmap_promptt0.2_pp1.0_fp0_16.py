import mmap
# Test mmap.mmap(0, 1, "shared", mmap.MAP_SHARED)

# import os
# os.system("pause")

import os
import sys
import time
import mmap
import struct

# This is the shared memory file.
# It must be created before this program is run.
# It must be deleted after this program is run.
# It must be readable and writable by all users.
# It must be at least as large as the struct below.
SHM_FILE = "/dev/shm/shm_example"

# This is the struct that will be written to shared memory.
# It must be the same size as the struct below.
# It must be the same size as the shared memory file.
# It must be the same size as the struct in the other program.
# It must be the same size as the struct in the C program.
class ShmStruct(object):
    _fields_ = [
        ("a", ctypes.c_int32),
        ("b", ctypes.c_int32),
        ("c", ctypes.c_int32),
       
