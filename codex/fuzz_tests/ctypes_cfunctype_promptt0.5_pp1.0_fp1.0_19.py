import ctypes
# Test ctypes.CFUNCTYPE

if __name__ == '__main__':
    # This test is based on the example at
    # http://docs.python.org/library/ctypes.html

    import sys
    import unittest
    from test.test_support import run_unittest

    class CFuncPtrTest(unittest.TestCase):
        def test_CFUNCTYPE(self):
            # Define a C callback function
            CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
            def py_callback(arg1, arg2):
                return arg1 * arg2

            # Convert the Python callback into a C callback
            c_callback = CALLBACK(py_callback)

            # Call the C callback via the ctypes callback
            self.assertEqual(c_callback(2, 3), 6)

            # Call the C callback directly from within Python
            func = c_callback.func
            func_ptr = c_callback.func_ptr
            self.assertEqual(func(2
