import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def function(n):
    return n + 5

p = FUNTYPE(function)
p(10)

# Converting C functions to Python with ctypes
# --------------------------------------------
#
# The ctypes module lets you access C functions from Python, but what if you
# want to call Python from C? The ctypes module includes a function called
# pythonapi, which lets you access the Python C API.
#
# The Python C API is a set of functions that let you manipulate Python objects
# and interpret the Python interpreter. Some of these functions are used to
# create new types, but most are used to manipulate objects. You can use the
# Python C API to create an extension module that can be used from Python.
#
# The Python C API is the hardest part of writing an extension module. It would
# be very hard to explain everything you need to know in this course. But
# because the use of ctypes is so common, I'll explain how to use the Python C
# API through ctypes.
#
# This example (from http://docs.python
