import weakref
# Test weakref.ref() for methods
import sys
class A:
    def __init__(self):
        self.a = 1
    def f(self):
        return self.a
    def g(self):
        return sys.getrefcount(self)

a = A()
r = weakref.ref(a.f)
f = r()
print(f())

r = weakref.ref(a.g)
print(r()())
x = r()
del a
print(x())
