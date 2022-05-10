import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# This test checks that gc.collect() returns the number of unreachable
# objects it found and collected.

import gc, weakref

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

# Create a cycle involving a tuple and a function.
def f():
    return t
t = (f,)

# Create a cycle involving a dict and a frame.
def g():
    d = {}
    d[0] = d
    return 1

# Create a cycle involving a list and a frame.
def h():
    l = []
    l.append(l)
    return 1

# Create a cycle involving a module and a dict.
import sys
d = {}
sys.modules[__name__] = d
d[__name__] = sys.modules

# Create a cycle involving a dict and a class.
d = {}
class M:
    pass
d[0] = M
M.d = d

# Create a
