import weakref
# Test weakref.ref() on a class instance.
import _weakref

class C:
    pass

o = C()
r = weakref.ref(o)
print(r())
print(r() is o)
print(r() is None)
o2 = C()
r2 = weakref.ref(o2)
print(r2() is o2)
print(r() is o2)
print(r() is None)

# Test weakref.proxy() on a class instance.
p = weakref.proxy(o)
print(p is o)
print(p.__class__ is C)
print(p is None)

# Test weakref.proxy() on a class instance with a __del__ method.
class C:
    def __del__(self):
        pass

o = C()
p = weakref.proxy(o)
print(p is o)
print(p.__class__ is C)
print(p is None)

# Test weakref.proxy() on a class instance with a __cmp__ method.
