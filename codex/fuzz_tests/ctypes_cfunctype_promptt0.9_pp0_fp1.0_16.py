import ctypes
# Test ctypes.CFUNCTYPE 
from ctypes import CFUNCTYPE


my_lib = ctypes.CDLL('my_shared_lib.dll')
subroutine = my_lib.subroutine
subroutine.argtypes = [ctypes.c_int, ctypes.c_int]
subroutine.restype = ctypes.c_float


# This is the test case:
callback  = CFUNCTYPE(c_int, c_int, c_int) 
subroutine(5, callback(5,5))
</code>
The error is as follows:
<code>subroutine(5, callback(5,5))
TypeError: integer argument expected, got instance
</code>


A:

It's not possible to create a ctypes <code>CFUNCTYPE</code> directly from a python function. You have to define a wrapper function which calls the python function, then call <code>CFUNCTYPE</code> for the wrapper. See https://docs.python.org/3/library/ctypes.html#callbacks
To illustrate, suppose we had
