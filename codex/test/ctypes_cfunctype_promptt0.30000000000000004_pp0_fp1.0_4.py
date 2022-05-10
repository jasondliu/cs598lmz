import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

# This is a function that takes a function pointer as an argument
# and calls it.

def callback(funcptr):
    funcptr()

# This is the function we want to pass to callback

