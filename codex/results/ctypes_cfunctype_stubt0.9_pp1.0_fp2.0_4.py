import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "spam"
fun.__name__ = 'hello'
print(fun())

"""
OUTPUT
