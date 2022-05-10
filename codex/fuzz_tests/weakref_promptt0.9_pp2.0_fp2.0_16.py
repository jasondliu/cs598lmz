import weakref
# Test weakref.ref() on something that does not support weak references.
import sys
from test import test_support

class Foo(object):
    pass

f = Foo()
r = weakref.ref(f)
e = weakref.ref(f, lambda a: 5)

# foo doesn't support weak references.
try:
    f.ref = r
except TypeError:
    pass
else:
    print("f.ref = r didn't raise TypeError")

e(f)
support.collect()

# An uncollectable object: a cycle of a function with a closure referring
# to itself.
def f():
    g()
    x = 5
    g()
def g():
    x = y
y = weakref.ref(f)
f()
a = weakref.WeakKeyDictionary()
a[f] = 1

# Test weakref.ref works with class instances.
class C(object):
    pass
c = C()
w = weakref.ref(c)
del c
support.collect()
#if w() is not None:
#   
