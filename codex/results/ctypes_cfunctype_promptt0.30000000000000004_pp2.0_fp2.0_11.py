import ctypes
# Test ctypes.CFUNCTYPE

from ctypes import *

# A function that takes a function pointer as argument
libc = CDLL(ctypes.util.find_library("c"))

# The prototype of the function that is passed as argument
# to the function above
CALLBACKFUNC = CFUNCTYPE(c_int, c_int, c_int)

# The function that is passed as argument to the function above
@CALLBACKFUNC
def callback(a, b):
    print("callback called with %d and %d" % (a, b))
    return a + b

# The function that takes a function pointer as argument
libc.test(callback)

# The function that takes a function pointer as argument
# and calls it with different arguments
libc.test2(callback, 1, 2)

# The function that takes a function pointer as argument
# and calls it with different arguments
libc.test3(callback, 3, 4)

# The function that takes a function pointer as argument
# and calls it with different arguments
libc.test4(callback, 5, 6)

