import ctypes
# Test ctypes.CFUNCTYPE by calling a user defined C function from Python

# Prototype of the ctype function
# This is the header file for the c function
CFUNCTYPE_func = ctypes.CFUNCTYPE(None, ctypes.c_float, ctypes.c_float)

# C function to print arguments and their sum
