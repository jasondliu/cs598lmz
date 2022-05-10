import types
# Test types.FunctionType
def f1(): pass
def f2(): pass
f3 = f1

assert isinstance(f1, types.FunctionType)
assert isinstance(f2, types.FunctionType)
assert isinstance(f3, types.FunctionType)

assert type(f1) is types.FunctionType
assert type(f2) is types.FunctionType
assert type(f3) is types.FunctionType

# Test types.BuiltinFunctionType
def f4(): pass
f5 = f4

assert isinstance(f4, types.BuiltinFunctionType)
assert isinstance(f5, types.BuiltinFunctionType)

assert type(f4) is types.BuiltinFunctionType
assert type(f5) is types.BuiltinFunctionType

# Test types.MethodType
def f6(): pass
class C:
    def m1(self): pass
    m2 = f6

assert isinstance(C.m1, types.MethodType)
assert isinstance(C.m2, types.MethodType)

assert type(C.m1) is types.
