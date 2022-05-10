import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello World"
fun()

#class myclass(object):
#    def __init__(self, a):
#        self.a = a
#    def __call__(self, *args, **kwargs):
#        return self.a
#f = myclass("Hello World")
#f()

class myclass(object):
    def __init__(self, a):
        self.a = a
    def __call__(self, *args, **kwargs):
        return self.a
f = myclass("Hello World")
fun = ctypes.CFUNCTYPE(ctypes.py_object)(f)
fun()
