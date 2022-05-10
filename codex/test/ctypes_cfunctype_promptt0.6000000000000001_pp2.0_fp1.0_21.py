import ctypes
# Test ctypes.CFUNCTYPE

def test_CFUNCTYPE():
    # Test basic operation
    try:
        ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
    except:
        print("Error: ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)")
        raise

    # Test first arg can be omitted
    try:
        ctypes.CFUNCTYPE(ctypes.c_int)
    except:
        print("Error: ctypes.CFUNCTYPE(ctypes.c_int)")
        raise

    # Test return type must be a ctypes type
    try:
        ctypes.CFUNCTYPE(int, ctypes.c_int)
    except TypeError:
        pass
    else:
        print("Error: ctypes.CFUNCTYPE(int, ctypes.c_int)")
        raise

    # Test argtypes must be a tuple
