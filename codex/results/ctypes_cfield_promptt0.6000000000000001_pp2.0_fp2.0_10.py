import ctypes
# Test ctypes.CField

if __name__ == "__main__":
    import test.test_support
    import ctypes.test.test_cfiled as test_cfiled

    test.test_support.run_unittest(test_cfiled.CFieldTestCase)
