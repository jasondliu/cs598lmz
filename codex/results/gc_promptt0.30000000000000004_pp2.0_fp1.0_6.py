import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# This test is intended to be run with the Python test driver, not
# directly.

import gc, weakref

class C:
    pass

# Create a cycle with a list and a dictionary.
x = []
y = {}
x.append(y)
y[0] = x

# Create a cycle with a function and a frame.
def f():
    pass

f.x = f

# Create a cycle with a function and a code object.
def g():
    pass

g.x = g.func_code

# Create a cycle with a class and a method.
class D:
    def __init__(self):
        self.x = self.m
    def m(self):
        pass

# Create a cycle with a class and a method.
class E:
    def __init__(self):
        self.x = self.m
    def m(self):
        pass

# Create a cycle with a class and a method.
class F:
    def __init__(self):
        self.x =
