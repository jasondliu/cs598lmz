import ctypes
ctypes.cast(ctypes.c_void_p(3), ctypes.c_char_p).value

import sys
import ctypes
libc = ctypes.cdll.LoadLibrary('libc.so.6')
