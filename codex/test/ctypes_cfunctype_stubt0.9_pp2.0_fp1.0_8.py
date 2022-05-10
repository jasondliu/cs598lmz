import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return global_var
#
# fun is a valid python callable, now turn it into a C object
#
cfun = ctypes.cast(fun, FUNTYPE)
#
# now run the resulting cfun
#
print(ctypes.py_object(cfun()))

#
# Now, we destroy global_var. This will break fun, but only when it is called
# again.
#

del global_var
print(ctypes.py_object(cfun()))
