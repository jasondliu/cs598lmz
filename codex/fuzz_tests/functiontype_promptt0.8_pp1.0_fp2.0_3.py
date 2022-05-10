import types
# Test types.FunctionType -- it's not precisely a wrapper for calls
# (return values are ignored and some arg checking is done), but it
# provides the ability to do an arbitrary function call from a string.
import sys

def f(x):
    "f doc"
    return f

def g(x):
    return g

def h():
    return h

def i():
    return i

class C:
    def f(self, x):
        return self.f
    def g(self, x):
        return self.g
    def h(self):
        return self.h
    def i(self):
        return self.i


#
# First, some tests of the type checking.

# This is a function
try:
    types.FunctionType(lambda: None, {})
except TypeError:
    pass
else:
    raise TestFailed

# This is not a code object
try:
    types.FunctionType(None, {})
except TypeError:
    pass
else:
    raise TestFailed

# This is not a namespace
try:
