import ctypes
# Test ctypes.CFUNCTYPE
#
#  This is a test of the ctypes.CFUNCTYPE() function.  It defines
#  a function pointer type, and then creates a function pointer
#  instance.  It calls the function pointer instance, and checks
#  that the result is correct.
#
import ctypes

try:
    ctypes.CFUNCTYPE
except AttributeError:
    print('SKIP')
    raise SystemExit

# Define the function pointer type.
CFuncPtr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# Define a function that takes an integer argument, doubles it, and
# returns the result.
def func(arg):
    return arg * 2

# Create a function pointer instance.
cfunc = CFuncPtr(func)

# Call it.
res = cfunc(41)

# Check the result.
if res != 82:
    print("FAILED")
