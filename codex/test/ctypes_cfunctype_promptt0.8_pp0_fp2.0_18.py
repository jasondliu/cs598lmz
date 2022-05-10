import ctypes
# Test ctypes.CFUNCTYPE()
# equivalent c code from http://docs.python.org/2/library/ctypes.html
#
# // prototype of the required callback function
# typedef void (*functype)(void);
# 
# // this function receives a function pointer as argument
# void callfunct(functype f)
# {
#     f();
# }

# The following uses ctypes to create a function pointer to
# callfunct() and then passes it the address of a python
# function.

from ctypes import *

#Python callback
def py_functype():
    print("py_functype()")
py_functype_pointer = CFUNCTYPE(None)(py_functype)

#define and load the lib
#lib = CDLL("/home/nicholas/Projects/pipython/python/scripts/libtest.so")
