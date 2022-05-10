import ctypes
# Test ctypes.CFUNCTYPE on every calling convention.
for cc in [
        ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int),
        ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int),
        ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int,
            ctypes.c_int),
        ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int,
            ctypes.c_int, ctypes.c_int),
        ]:
    f = cc(add)
    assert type(f(1, 2)) is int
    assert f(10, 20) == 30

# This calls ctypes_add directly, as a ctypes.CFUNCTYPE'd function
def test(add):
    add_int = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_
