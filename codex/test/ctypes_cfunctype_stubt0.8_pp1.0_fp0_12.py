import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 3
result = fun()
print(result, type(result))

@FUNTYPE
def fun():
    return "spam"
result = fun()
print(result, type(result))

@FUNTYPE
def fun():
    class A(object):
        pass
    return A()
result = fun()
print(result, type(result))
