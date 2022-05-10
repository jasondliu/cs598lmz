import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

print(fun())

import sys
from ctypes import *

libc = CDLL("libc.so.6")
printf = libc.printf
printf("Hello, World\n")
printf("%s, %d\n", "hello", 42)

from ctypes import *

class Data(Structure):
    _fields_ = [("a", c_int), ("b", c_char)]

data = Data(42, b"hello")
print(data.a, data.b)

from ctypes import *

libc = CDLL("libc.so.6")
libc.printf("Hello, World\n")

from ctypes import *

libc = CDLL("libc.so.6")

printf = libc.printf
printf.argtypes = [c_char_p]
printf("Hello, World\n")

from ctypes import *

libc = CDLL("libc.so.6")

printf = libc.printf
printf.argtypes = [c_char_p]

