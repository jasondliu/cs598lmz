import ctypes
# Test ctypes.CField

if __name__ == "__main__":
    import test.test_support

    # The code below tries to define a non-character type
    # field of a structure, which crashes on many platforms.
    class X(ctypes.Structure):
        _fields_ = [("_", ctypes.CField)]

    try:
        X()
    except TypeError:
        pass
    else:
        raise TestFailed("CField test failed")

    test.test_support.run_unittest(__name__)
