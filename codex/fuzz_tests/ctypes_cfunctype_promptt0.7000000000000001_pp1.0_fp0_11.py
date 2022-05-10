import ctypes
# Test ctypes.CFUNCTYPE

def test_builtin():
    from ctypes import byref, c_char_p, string_at

    for libname in ("libc.dylib", "libSystem.dylib"):
        libc = ctypes.cdll.LoadLibrary(libname)
        c_strlen = libc.strlen
        c_strlen.argtypes = ctypes.c_char_p,
        c_strlen.restype = ctypes.c_size_t

        def strlen(s):
            return c_strlen(s)

        cfunc = ctypes.CFUNCTYPE(ctypes.c_size_t, ctypes.c_char_p)(strlen)
        assert cfunc("abc") == 3
        assert cfunc(b"abc") == 3

        assert cfunc(byref(c_char_p(b"abc"))) == 3

        # Test passing a unicode object.  We expect a bytes object to be
        # returned.
        assert cfunc(u"abc") == 3

        # Test passing a unicode object.  We
