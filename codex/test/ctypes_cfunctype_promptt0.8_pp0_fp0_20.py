import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_int)
# See bpo-24152: "ctypes.CFUNCTYPE(ctypes.c_int) leads to a crash".
# The problem only happens with a debug build of Python (ex: --with-pydebug).
class_type = ctypes.CFUNCTYPE(ctypes.c_int)

# Test ctypes.c_void_p.from_buffer()
# See bpo-31646
buf = bytearray(b"Hello")
