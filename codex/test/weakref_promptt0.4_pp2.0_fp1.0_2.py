import weakref
# Test weakref.ref()
import sys
import gc
import weakref

class A:
    pass

a = A()
r = weakref.ref(a)
assert r() is a
del a
gc.collect()
assert r() is None

# Test weakref.proxy()
import sys
import gc
import weakref

class A:
    pass

a = A()
p = weakref.proxy(a)
assert p is a
del a
gc.collect()
try:
    p.foo
except ReferenceError:
    pass
else:
    assert False, "weakref.proxy() did not raise ReferenceError"

# Test weakref.getweakrefcount()
import sys
import gc
import weakref

class A:
    pass

a = A()
r = weakref.ref(a)
assert weakref.getweakrefcount(a) == 1

# Test weakref.getweakrefs()
import sys
import gc
import weakref

class A:
    pass

a = A()
