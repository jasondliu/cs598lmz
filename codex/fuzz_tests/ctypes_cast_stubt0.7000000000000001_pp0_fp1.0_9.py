import ctypes
ctypes.cast(ctypes.c_void_p(3), ctypes.c_char_p).value

import sys
import ctypes
libc = ctypes.cdll.LoadLibrary('libc.so.6')
def mem_map(addr, length):
    return ctypes.cast(
        libc.mmap(
            ctypes.c_void_p(addr),
            length,
            ctypes.c_int(0x05), # PROT_READ|PROT_WRITE
            ctypes.c_int(0x21), # MAP_SHARED|MAP_FIXED
            ctypes.c_int(-1), # fd
            ctypes.c_i
