import types
# Test types.FunctionType
def f(): pass

import types
assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)

import types
assert isinstance(type, types.BuiltinFunctionType)

# Test types.MethodType
class C(object):
    def m(self): pass

import types
assert isinstance(C.m, types.MethodType)
assert isinstance(C.m, types.BuiltinMethodType)

# Test types.LambdaType
l = lambda: None

import types
assert isinstance(l, types.LambdaType)

# Test types.GeneratorType
def g(): yield

import types
assert isinstance(g(), types.GeneratorType)
assert isinstance(g(), types.BuiltinFunctionType)

# Test types.CodeType
def f(): pass

import types
assert isinstance(f.__code__, types.CodeType)

# Test types.TracebackType
def f(): pass

import types
try:
    f()
except:
    import sys

