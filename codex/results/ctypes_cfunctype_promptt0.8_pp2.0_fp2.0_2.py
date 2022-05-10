import ctypes
# Test ctypes.CFUNCTYPE
cf = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
f = cf((lambda x: 127))
assert f(42) == 127
# Test ctypes.byref()
l = ctypes.c_long(1)
assert ctypes.byref(l).contents.value == 1
assert l.value == 1
# Test ctypes.cast()
cp = ctypes.cast(ctypes.c_char_p("abc"), ctypes.c_void_p)
assert ctypes.cast(cp, ctypes.c_char_p).value == b"abc"
# Test ctypes.pointer()
p = ctypes.pointer(ctypes.c_long(1))
assert p.contents.value == 1
assert ctypes.addressof(p.contents) == ctypes.addressof(p.contents)
# Test ctypes.sizeof()
assert ctypes.sizeof(ctypes.c_long) == 8
# Test ctypes.string_at()
assert ctypes.string_at(
