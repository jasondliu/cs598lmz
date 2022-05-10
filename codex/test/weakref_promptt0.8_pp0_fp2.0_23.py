import weakref
# Test weakref.ref on objects which do not support weakrefs

import copy_reg, gc, pickle, weakref, types

# Testing some basic operations on weakrefs
a = []
x = weakref.ref(a)
def f():
    global a
    b = a
    a = None
    return b
del a
assert f() is None
gc.collect()
assert x() is None

a = []
x = weakref.ref(a)
del a
assert x() is not None
del x
gc.collect()
assert sys.getrefcount(a) == 1

a = []
x = weakref.ref(a)
y = copy.copy(x)
assert y() is a
assert x() is y()
z = copy.deepcopy(y)
assert z() is a
del y
del z
gc.collect()
assert x() is a
del x

a = []
x = weakref.ref(a)
y = pickle.dumps(x)
del x
gc.collect()
assert a is not None
z = pick
