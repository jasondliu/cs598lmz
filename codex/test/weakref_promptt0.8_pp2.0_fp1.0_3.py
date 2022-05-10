import weakref
# Test weakref.ref
import gc
import sys
from test.support import check_sizeof, requires_resource

# Test the callback itself.

_called = []

class A:
    pass

def callback(wr, _called=_called):
    _called.append(wr)

a = A()

# Call once.
wr = weakref.ref(a, callback)
del a
gc.collect()
assert len(_called) == 1

# Call again.
a = A()
wr = weakref.ref(a)
del a
gc.collect()
assert len(_called) == 1

# Call with a keyword argument.
del _called[:]
a = A()
_called.append(0)
wr = weakref.ref(a, callback, 0)
del a
gc.collect()
assert len(_called) == 2

# Test weakref.ref.__call__

called = []

class A:
    pass

def callback(wr, called=called):
    called.append(wr)

a = A()

# Call once
