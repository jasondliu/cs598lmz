import ctypes
# Test ctypes.CField
import ctypes.util

if ctypes.sizeof(ctypes.c_longdouble) == ctypes.sizeof(ctypes.c_double):
    # 64-bit platform
    class X(ctypes.Structure):
        _fields_ = [("a", ctypes.c_double),
                    ("b", ctypes.c_double)]
else:
    # 32-bit platform
    class X(ctypes.Structure):
        _fields_ = [("a", ctypes.c_double),
                    ("b", ctypes.c_longdouble)]

x = X()
x.a = 1.2345
x.b = 6.78901
print(x.a, x.b)

# Test ctypes.c_buffer
import array

buf = ctypes.c_buffer(b"Hello World")
print(buf[:6])

# Test ctypes.c_char_p
import sys

if sys.platform == "win32":
    libc_name = ctypes.util.find_msvcrt()
else:

