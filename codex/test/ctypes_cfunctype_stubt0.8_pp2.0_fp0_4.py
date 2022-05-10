import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello world"

print(fun())
# 'hello world'
print(type(fun))
# <class 'ctypes.CFUNCTYPE'>
print(type(fun(None)))
# &lt;class 'bytes'&gt;
