import weakref
# Test weakref.ref(c) and
# weakref.ref(a)() == weakref.ref(b)() == weakref.ref(c)() == c

class C(object):
    pass

c = C()

a = weakref.ref(c)
b = weakref.ref(a)

