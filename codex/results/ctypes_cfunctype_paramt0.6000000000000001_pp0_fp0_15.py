import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def py_func(x):
    return x * x
func = FUNTYPE(py_func)
print func(3)

class A(object):
    def __init__(self):
        self.x = 1

def func(obj):
    obj.x = 2

a = A()
func(a)
print a.x

class Test(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

t = Test(1, 2)
print t.a, t.b

#tuple
t = (1, 2, 3)
print t
print t[0]
print t[0:2]

#dictionary
d = {'name': 'foo', 'age': 20}
print d
print d['name']
print d['age']
print d.keys()
print d.values()
print d.items()

#list
l = [1, 2, 3, 4]
print l

