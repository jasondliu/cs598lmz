import weakref
# Test weakref.ref() with a class instance.
import __main__
import sys

class C:
    pass

c = C()
r = weakref.ref(c)

# Test basic ref() functionality
assert r() is c
assert r() is not None

# Test ref() with a subclass
class D(C):
    pass

d = D()
r = weakref.ref(d)
assert r() is d

# Test ref() with a class instance
class E:
    pass

e = E()
r = weakref.ref(e)
assert r() is e

# Test ref() with a class instance from a different module
# (i.e. __main__)
m = __main__.C()
r = weakref.ref(m)
assert r() is m

# Test ref() with a class instance from a different module
# (i.e. sys)
s = sys.getrefcount
r = weakref.ref(s)
assert r() is s

# Test ref() with a class instance from a different module
# (i.e
