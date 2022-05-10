import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_int)
# See bpo-24152: "ctypes.CFUNCTYPE(ctypes.c_int) leads to a crash".
# The problem only happens with a debug build of Python (ex: --with-pydebug).
class_type = ctypes.CFUNCTYPE(ctypes.c_int)

# Test ctypes.c_void_p.from_buffer()
# See bpo-31646
buf = bytearray(b"Hello")
p = ctypes.c_void_p.from_buffer(buf)
print(p.value)

# Test ctypes.c_void_p.from_address()
# See bpo-29984
if sizeof(c_void_p) == sizeof(c_size_t):
    var = c_byte * 10
    p = pointer((c_byte * 10).from_address(id(var)))
    print(p[0])  # This crashes

# Test ctypes.memmove_s()
# See bpo-33738
try:

