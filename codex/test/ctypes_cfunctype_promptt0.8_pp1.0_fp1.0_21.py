import ctypes
# Test ctypes.CFUNCTYPE
# EXPECTED: OK

def dummy_callback(*args):
    return False

CB_BOOL = ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_double)

def test_callback(callback):
    assert(callback(3.14) == False)

test_callback(CB_BOOL(dummy_callback))
print("OK")
