import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def callback(fun):
    return fun()

class Foo(object):
    def __init__(self, fun):
        self.fun = fun
    def __call__(self):
        return self.fun()

def main():
    fun = Foo(fun)
    callback(fun)

