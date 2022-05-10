import ctypes
# Test ctypes.CFUNCTYPE
# This will be needed for the callback functions

# The callback function
def print_number(number):
    print(number)

# The callback function prototype
CMPFUNC = ctypes.CFUNCTYPE(None, ctypes.c_int)

# The callback function wrapper
def py_print_number(number):
    return CMPFUNC(print_number)(number)

# The function that takes the callback function
def test_callback(callback):
    callback(1)

# The function that takes the callback function wrapper
def test_py_callback(callback):
    callback(1)

# Test the callback function
test_callback(print_number)

# Test the callback function wrapper
test_py_callback(py_print_number)

# Test the callback function wrapper with a lambda expression
test_py_callback(lambda number: print(number))

# Test the callback function wrapper with a lambda expression
# This is the most concise way
test_py_callback(CMPFUNC(lambda number: print(number)))

# Test the callback function wrapper with a
