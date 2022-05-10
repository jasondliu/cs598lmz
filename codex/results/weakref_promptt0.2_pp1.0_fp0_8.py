import weakref
# Test weakref.ref() on a class.
class C:
    pass

r = weakref.ref(C)
assert r() is C
# Test weakref.ref() on an instance.
class C:
    pass

o = C()
r = weakref.ref(o)
assert r() is o
# Test weakref.ref() on a function.
def f():
    pass

r = weakref.ref(f)
assert r() is f
# Test weakref.ref() on a method.
class C:
    def f(self):
        pass

o = C()
r = weakref.ref(o.f)
assert r() is o.f
# Test weakref.ref() on a builtin.
r = weakref.ref(len)
assert r() is len
# Test weakref.ref() on a class method.
class C:
    @classmethod
    def f(cls):
        pass

r = weakref.ref(C.f)
assert r() is C.f
# Test weakref.ref() on a static method.

