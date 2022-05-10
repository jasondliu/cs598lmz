import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hello'

class A(object):
    def __init__(self):
        self.a = fun

a = A()
print(a.a())
</code>

