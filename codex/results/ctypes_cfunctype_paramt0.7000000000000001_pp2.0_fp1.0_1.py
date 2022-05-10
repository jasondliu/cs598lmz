import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# Simulate an Exception to test the error handling
def test_exception():
    raise Exception('Expected exception thrown')

def test_py_exception():
    raise RuntimeError('Expected Python exception')

# Create a couple of callback functions
def add(val1, val2):
    return val1 + val2

def sub(val1, val2):
    return val1 - val2

def load_and_call(libname):
    # Load the dynamic library
    lib = ctypes.CDLL(libname)

    # Set the return types of the callback functions
    lib.add.restype = ctypes.c_int
    lib.sub.restype = ctypes.c_int

    # Set the argument types of the callback functions
    lib.add.argtypes = [ctypes.c_int, ctypes.c_int]
    lib.sub.argtypes = [ctypes.c_int, ctypes.c_int]

    # Create a couple
