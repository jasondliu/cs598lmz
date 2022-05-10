import weakref
# Test weakref.ref().
import _weakref

class Foo:
    def __init__(self):
        self.a = 0
    def set_a(self,a):
        self.a = a

f = Foo()
x = Foo()
p = weakref.ref(x)

f.set_a(42)
print f.a

x.set_a(47)
print p().a

print p().__class__
