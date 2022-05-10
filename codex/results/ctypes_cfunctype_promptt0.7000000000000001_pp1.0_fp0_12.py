import ctypes
# Test ctypes.CFUNCTYPE
from ctypes.wintypes import BOOL, HANDLE
from ctypes import POINTER, WINFUNCTYPE, windll

LPVOID = ctypes.c_void_p
DWORD = ctypes.c_uint32
WORD = ctypes.c_uint16
LPCSTR = ctypes.c_char_p

DWORD_PTR = DWORD
ULONG_PTR = ctypes.c_uint32  # or c_ulong
SIZE_T = ULONG_PTR

class MEMORY_BASIC_INFORMATION(ctypes.Structure):
    _fields_ = [
        ('BaseAddress', LPVOID),
        ('AllocationBase', LPVOID),
        ('AllocationProtect', DWORD),
        ('RegionSize', SIZE_T),
        ('State', DWORD),
        ('Protect', DWORD),
        ('Type', DWORD),
    ]

class SYSTEM_INFO(ctypes.Structure):
    _fields_ = [
        ('wProcessorArchitecture', WORD),
        ('wReserved
