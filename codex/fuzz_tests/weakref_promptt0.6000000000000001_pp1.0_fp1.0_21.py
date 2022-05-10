import weakref
# Test weakref.ref()

import weakref

class C:
    pass

# Weak reference to an instance of the class.
c = C()
r = weakref.ref(c)
print r() is c
print r() == c

# Weak reference to an instance of a built-in class.
t = (1, 2, 3)
r = weakref.ref(t)
print r() is t
print r() == t

# Weak reference to an instance of a built-in class.
s = "abc"
r = weakref.ref(s)
print r() is s
print r() == s

# Weak reference to a function.
def f():
    pass

r = weakref.ref(f)
print r() is f
print r() == f

# Weak reference to a function.
def f():
    pass

r = weakref.ref(f)
print r() is f
print r() == f

# Weak reference to a method.
class C(object):
    def meth(self):
        pass

c = C()
r =
