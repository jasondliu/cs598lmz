import types
# Test types.FunctionType and types.MethodType

def f():
    pass

class C:
    def m(self):
        pass

print(type(f) == types.FunctionType)
print(type(C.m) == types.MethodType)
print(type(C().m) == types.MethodType)

# Test types.GeneratorType

def g():
    yield 1

print(type(g()) == types.GeneratorType)

# Test types.TracebackType

import sys
try:
    1/0
except:
    tb = sys.exc_info()[2]
print(type(tb) == types.TracebackType)

# Test types.BuiltinFunctionType

print(type(abs) == types.BuiltinFunctionType)
print(type(C.m) != types.BuiltinFunctionType)
