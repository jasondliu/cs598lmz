import weakref
# Test weakref.ref()

import weakref
import gc

class Foo:
    pass

a = Foo()
r = weakref.ref(a)
assert r() is a
b = Foo()

# Test that weakref.ref() accepts an object that is not weakrefable
# but whose type is weakrefable.

class NoWeakRef:
    pass

class HasWeakRef:
    pass

class A:
    pass

class B(A):
    pass

a = NoWeakRef()
b = B()

assert weakref.ref(a)() is a
assert weakref.ref(b)() is b

# Test that weakref.ref() fails for a non-weakrefable type

class NotWeakRefable:
    pass

a = NotWeakRefable()

try:
    weakref.ref(a)
except TypeError:
    pass
else:
    print("expected TypeError")

a = HasWeakRef()
b = B()

def callback(r):
    global a
    a = None

