import ctypes
# Test ctypes.CFUNCTYPE(None)
def _test_callback_1():
    print("_test_callback_1")

_test_callback_1_t = ctypes.CFUNCTYPE(None)
_test_callback_1_t(_test_callback_1)()  # prints "_test_callback_1"

# Test ctypes.CFUNCTYPE(None, ctypes.c_int)
def _test_callback_2(n):
    print("_test_callback_2: %d" % n)

_test_callback_2_t = ctypes.CFUNCTYPE(None, ctypes.c_int)
_test_callback_2_t(_test_callback_2)(42)  # prints "_test_callback_2: 42"

# Test ctypes.CFUNCTYPE(ctypes.c_int)
def _test_callback_3():
    print("_test_callback_3")
    return 42

_test_callback_3_t = ctypes.CFUNCTYPE(ctypes.c_int)
