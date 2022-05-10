import ctypes
libc = ctypes.CDLL("libc.so.6")
try:
    memmove = libc.memmove
except AttributeError:
    raise SkipTest("skipping test due to missing symbol")
retval = memmove(0, 0, 1)
