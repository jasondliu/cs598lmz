import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
class A(object):
    def __init__(self):
        self.b = B(self)
    def __del__(self):
        print("deleting A")
class B(object):
    def __init__(self, a):
        self.a = a
    def __del__(self):
        print("deleting B")
def f():
    a = A()
a = A()
a = None
b = B(a)
a = B(b)
a = None
b = None
gc.collect()
gc.collect()

# Test gc.get_debug
print(gc.get_debug())


def f():
    print("hello");print("hi");
import sys;sys.stdout.write("Hi")
print("hello");print("hi")

f = lambda x: 2*x
f(2)

def f(x): return 2*x
f(2)

class C:
    def __init__(self):
        self._x = None
    def getx(self):
        return
