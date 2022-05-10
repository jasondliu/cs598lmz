import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def callfun():
    return fun()

assert callfun() == "hello"
print('TEST SUCEEDED!')
