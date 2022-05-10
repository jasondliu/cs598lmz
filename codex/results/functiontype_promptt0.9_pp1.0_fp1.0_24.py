import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)

# Test types.MethodType
def f(): pass
class C:
    def g(self): pass
assert isinstance(f, types.MethodType)
assert isinstance(C.g, types.MethodType)
assert isinstance(C().g, types.MethodType)

# Test types.BuiltinFunctionType
assert isinstance(__import__, types.BuiltinFunctionType)
assert isinstance(int, types.BuiltinFunctionType)
assert isinstance(iter, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
assert isinstance([].append, types.BuiltinMethodType)
assert isinstance({}.get, types.BuiltinMethodType)

# Test types.ModuleType
assert isinstance(types, types.ModuleType)
assert isinstance(sys, types.ModuleType)

# Test types.CodeType
import dis
assert isinstance(f.__code__, types.CodeType)
assert isinstance(g.__code__, types.CodeType)
assert isinstance
