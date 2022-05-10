import weakref
# Test weakref.ref() on a builtin object
class C:
    pass
c = C()
r = weakref.ref(c)
if r() is not c:
    raise RuntimeError
# Test weakref.ref() on a class instance
class C:
    pass
c = C()
r = weakref.ref(c)
if r() is not c:
    raise RuntimeError
# Test weakref.ref() on a class instance with a __del__ method
class C:
    def __del__(self):
        pass
c = C()
r = weakref.ref(c)
if r() is not c:
    raise RuntimeError
# Test weakref.ref() on a method
class C:
    def f(self):
        pass
c = C()
r = weakref.ref(c.f)
if r() is not c.f:
    raise RuntimeError
# Test weakref.ref() on a method with a __del__ method
class C:
    def f(self):
        pass
    def __del__(self):
        pass
c = C()
