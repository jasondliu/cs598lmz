import ctypes
# Test ctypes.CFUNCTYPE
if 0:  # The following code is untested and fails
    def func(n):
        return n * (n + 1)

    cf = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
    a = cf(func)
    assert a(2) == 3

# Test ctypes calling convention
# TODO: same calling convention as MSVC
if 0:  # The following code is untested and probably buggy
    cdll.msvcrt.sprintf

    for cc in [ctypes.cdecl, ctypes.WINFUNCTYPE]:
        @cc(ctypes.c_int, ctypes.py_object)
        def func(n):
            return n * (n + 1)

        a = func(2)
        assert a == 3

# Test ctypes POINTER(...)
if 0:  # The following code is untested and probably buggy
    n = ctypes.c_int()
    adr = ctypes.c_void_p.from_address(id(n))
