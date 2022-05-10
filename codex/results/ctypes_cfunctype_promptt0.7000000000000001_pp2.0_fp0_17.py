import ctypes
# Test ctypes.CFUNCTYPE.
def test():
    # This function is called by the ctypes wrapper.
    def f(i, s):
        return s * i

    # Create a ctypes wrapper.
    F = ctypes.CFUNCTYPE(ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p)
    f2 = F(f)

    # Make sure it works as we expect.
    assert f2(2, b"ab") == b"abab"

    # The following is a bug in llvmlite 0.25.0:
    # TypeError: expected bytes, got str
    assert f2(2, "ab") == "abab"
