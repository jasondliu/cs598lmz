import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun(): #<- this is the python function
    pass

cfun = FUNTYPE(fun) #<- this is the ctypes function

print(cfun)
print(fun)
