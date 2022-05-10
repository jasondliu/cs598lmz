import weakref
# Test weakref.ref() on a class instance.
import weakref


class C:
    pass


c = C()
r = weakref.ref(c)
c2 = r()
print(c2 is c)
del c
print(r() is None)
# Test weakref.ref() on a class instance.
import weakref


class C:
    pass


c = C()
r = weakref.ref(c)
c2 = r()
print(c2 is c)
del c
print(r() is None)
# Test weakref.ref() on a class instance.
import weakref


class C:
    pass


c = C()
r = weakref.ref(c)
c2 = r()
print(c2 is c)
del c
print(r() is None)
# Test weakref.ref() on a class instance.
import weakref


class C:
    pass


c = C()
r = weakref.ref(c)
c2 = r()
print(c2 is c)
del c
