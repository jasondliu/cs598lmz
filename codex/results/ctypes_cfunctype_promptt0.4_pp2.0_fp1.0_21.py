import ctypes
# Test ctypes.CFUNCTYPE

if __name__ == "__main__":
    from test.support import run_unittest

    run_unittest(CFuncPtrTestCase)
