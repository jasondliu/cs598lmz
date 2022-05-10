import mmap
import os
import sys
import time

from collections import namedtuple
from ctypes import *
from ctypes.wintypes import *

# http://msdn.microsoft.com/en-us/library/aa383751(VS.85).aspx
class MEMORY_BASIC_INFORMATION(Structure):
    _fields_ = [
        ("BaseAddress", PVOID),
        ("AllocationBase", PVOID),
        ("AllocationProtect", DWORD),
        ("RegionSize", SIZE_T),
        ("State", DWORD),
        ("Protect", DWORD),
        ("Type", DWORD),
    ]

# http://msdn.microsoft.com/en-us/library/aa383751(VS.85).aspx
class SYSTEM_INFO(Structure):
    _fields_ = [
        ("wProcessorArchitecture", WORD),
        ("wReserved", WORD),
        ("dwPageSize", DWORD),
        ("lpMinimumApplicationAddress", LPVOID),
        ("lpMaximumApplicationAddress", LPVOID),

