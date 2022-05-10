import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun(): #<- this is the python function
    pass

cfun = FUNTYPE(fun) #<- this is the ctypes function

print(cfun)
print(fun)
print(cfun.__code__)
print(fun.__code__)

print(cfun.__code__.co_code)
print(fun.__code__.co_code)

print(cfun.__code__.co_code == fun.__code__.co_code)
print(cfun.__code__.co_code is fun.__code__.co_code)

print(cfun.__code__.co_code.__hash__())
print(fun.__code__.co_code.__hash__())

print(cfun.__code__.co_code.__hash__() == fun.__code__.co_code.__hash__())
print(cfun.__code__.co_code.__hash__() is fun.__code__.co_code.__hash__())

print(cfun.__code__.co_code.
