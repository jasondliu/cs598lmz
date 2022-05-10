import ctypes
# Test ctypes.CFUNCTYPE
#
# Python source

from ctypes import *

def my_callback(a, b):
    print "in my_callback", a, b
    return a / b

cb_type = CFUNCTYPE(c_int, # return type
                    c_int, # argument types
                    c_int)
my_callback_func = cb_type(my_callback)
dividend = 10
divisor = 5

print "dividing", dividend, "by", divisor

print "result (should be 2):",
print my_callback_func(dividend, divisor)
