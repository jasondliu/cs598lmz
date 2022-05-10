import types
types.MethodType(lambda self: None, None, object)

# Test for SF bug #1409796:  __del__() methods in extension
# classes didn't always get called.

class C:
    def __del__(self):
        global called
        called = 1

import gc
gc.collect()
called = 0
c = C()
c.x = C()
del c
gc.collect()
assert called

# Test for SF bug #1424489:  weakref callbacks weren't being
# called for objects with __del__() methods.

import weakref

class C:
    def __del__(self):
        global called
        called = 1

called = 0
c = C()
r = weakref.ref(c)
del c
gc.collect()
assert called

# Test for SF bug #1424506:  weakref callbacks weren't being
# called for objects with __del__() methods if the referent
# contained a cycle.

import weakref

class C:
    def __init__(self, x):

