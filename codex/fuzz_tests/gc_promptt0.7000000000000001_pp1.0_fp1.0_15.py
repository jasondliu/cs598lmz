import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A: pass
a = A()
w = weakref.ref(a)
del a
gc.collect()
print w() is None
# Test a basic cycle.
class A: pass
a = A()
a.b = a
w = weakref.ref(a)
del a
gc.collect()
print w() is None
# Test a cycle across module boundaries.
import gc, weakref, os
class A: pass
a = A()
m = weakref.ref(a)
del a
os.system("""python -c "
import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
class A: pass
a = A()
a.b = a
w = weakref.ref(a)
del a
gc.collect()
print w() is None
" > %s""" % TESTFN)
gc.collect()
print m() is None
# The following tests check the value of the attribute dict of the object
# when the last strong reference to the object is removed.
from weakref import WeakKeyDictionary
class
