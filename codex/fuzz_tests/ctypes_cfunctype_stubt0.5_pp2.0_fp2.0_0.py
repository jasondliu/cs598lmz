import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print fun()

def fun2():
    return "hello"

print fun2()

#fun2.__name__ = "fun2"
#print fun2()

class A(object):
    def __init__(self):
        self.name = "A"
    def fun3(self):
        return "hello"

a = A()
print a.fun3()
