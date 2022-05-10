import ctypes
# Test ctypes.CFUNCTYPE by calling a user defined C function from Python

# Prototype of the ctype function
# This is the header file for the c function
CFUNCTYPE_func = ctypes.CFUNCTYPE(None, ctypes.c_float, ctypes.c_float)

# C function to print arguments and their sum
lib = ctypes.cdll.LoadLibrary("./libadd.so")

# Python function calls C library and C function
@CFUNCTYPE_func
def call_CFUNCTYPE_func(arg1, arg2):
    print("In Python call_CFUNCTYPE_func")
    print("args:",arg1,arg2)
    print("arg1+arg2:", lib.add(arg1,arg2))
    
# Calling the python function
call_CFUNCTYPE_func(2,2)

# Must be run from terminal: python call_func.py
# Output: 
# In Python call_CFUNCTYPE_func
# args: 2.0 2.0
# arg1+arg2:
