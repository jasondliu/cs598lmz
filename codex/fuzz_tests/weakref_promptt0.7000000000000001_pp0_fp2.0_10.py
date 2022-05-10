import weakref
# Test weakref.ref() on functions
def f():
    pass
wr = weakref.ref(f)
print wr() is f
del f
print wr() is None
# Test weakref.ref() on methods
class C:
    def f(self):
        pass
c = C()
wr = weakref.ref(c.f)
print wr() is c.f
del c
print wr() is None
# Test weakref.ref() on class methods
class C:
    @classmethod
    def f(cls):
        pass
wr = weakref.ref(C.f)
print wr() is C.f
del C
print wr() is None
# Test weakref.ref() on static methods
class C:
    @staticmethod
    def f():
        pass
wr = weakref.ref(C.f)
print wr() is C.f
del C
print wr() is None

# Test weakref.proxy() on functions
def f():
    pass
p = weakref.proxy(f)
print p is f
del f
try:
    f()
except
