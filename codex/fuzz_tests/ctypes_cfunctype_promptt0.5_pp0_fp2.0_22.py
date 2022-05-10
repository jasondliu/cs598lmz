import ctypes
# Test ctypes.CFUNCTYPE(None)()
try:
    ctypes.CFUNCTYPE(None)()
except TypeError:
    print('SKIP')
    raise SystemExit

import _ctypes_test

# Python function with no arguments
def func():
    pass

# Python function with one argument
def func2(arg1):
    pass

# Python function with variable number of arguments
def func3(*args):
    pass

# Python function with variable number of arguments
def func4(arg1, *args):
    pass

# Python function with variable number of arguments
def func5(arg1, arg2, *args):
    pass

# Python function with variable number of arguments
def func6(arg1, arg2, arg3, *args):
    pass

# Python function with variable number of arguments
def func7(arg1, arg2, arg3, arg4, *args):
    pass

# Python function with variable number of arguments
def func8(arg1, arg2, arg3, arg4, arg5, *args):
    pass

# Python function
