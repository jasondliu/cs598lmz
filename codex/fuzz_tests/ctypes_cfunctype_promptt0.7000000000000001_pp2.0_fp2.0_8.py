import ctypes
# Test ctypes.CFUNCTYPE().
# Also test that you can pass a ctypes instance as a function argument.
import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

functype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

counter = 0

def callback(arg):
    global counter
    counter += arg
    return 0

CALLBACK = functype(callback)

lib.set_callback(CALLBACK)

for i in range(5):
    lib.do_callback(i)

print(counter)
assert counter == 10
