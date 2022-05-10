import ctypes
# Test ctypes.CFUNCTYPE
libc = CDLL("libc.so.6")

func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(
        lambda x, y: x + y)
print func(1, 2)
# 3

func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int,
        use_errno=True, use_last_error=True)(
        lambda x, y: libc.puts("Hello, world"))
print func(1, 2)
# Hello, world
# -1

print "errno:", ctypes.get_errno()
# 0
print "last_error:", ctypes.get_last_error()
# -1
import ctypes
# Test ctypes.POINTER
import ctypes
libc = CDLL("libc.so.6")

# c_void_p is required on x64 to receive a void *.
# On x86, using c_int is enough
