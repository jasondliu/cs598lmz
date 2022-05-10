import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1
fun()
 
# output:
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# File "test.py", line 2, in fun
# SystemError: error return without exception set
# 
# In contrast, if the return value is a ctypes object, then the
# SystemError is not thrown:

import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)
@FUNTYPE
def fun():
    return 1
fun()
 
# output:
# 1
# 
# Interestingly, the same effect is observed if the function
# returns an int:

import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)
@FUNTYPE
def fun():
    return 1
fun()
 
# output:
# 1
# 
# It seems that this is a consequence of the callable object in
# these two cases being the same object as the function object
# itself (rather than a wrapper object that delegates to the
# function).
