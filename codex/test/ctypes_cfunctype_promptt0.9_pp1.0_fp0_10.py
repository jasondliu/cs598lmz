import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_char) as a callback
# This is used in the happybase module, but it turns
# out I don't need to use it with the happybase module.

# This example was taken from
# http://stackoverflow.com/questions/20991539/python-ctypes-callback-function

# This function is taking a ctypes.c_char as input and returning a c_char.
# I believe this would be an appropriate calling convention for a 
# callback from lua to python that returns an integer, if we decide to use
# it anyway. 
