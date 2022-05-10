import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("simple call")
result = test_pyobject_invocable(fun)
print(result)

result = test_pyobject_invocable(None)
print(result)
result = test_pyobject_invocable(int)
print(result)
result = test_pyobject_invocable(float)
print(result)
result = test_pyobject_invocable("foo")
print(result)

class C:
    pass
result = test_pyobject_invocable(C)
print(result)
