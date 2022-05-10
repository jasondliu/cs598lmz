import types
# Test types.FunctionType()
def f(a, b, c):
    pass
assert type(f) == types.FunctionType

def g():
    def h():
        pass
    return h
assert type(g()) == types.FunctionType

class A(object):
    def __init__(self, a, b, c):
        pass
assert type(A.__init__) == types.MethodType

import _types
assert type(A.__init__) == _types.MethodType

class B(object):
    def __init__(self, a, b, c):
        def m(a, b, c):
            pass
        self.m = m

assert type(B().m) == types.FunctionType

# Test types.BuiltinFunctionType()
def f(a, b, c):
    pass
assert type(f) != types.BuiltinFunctionType

assert type(len) == types.BuiltinFunctionType

import sys
assert type(sys.exit) == types.BuiltinFunctionType

# Test types.MethodType()
def f(a
