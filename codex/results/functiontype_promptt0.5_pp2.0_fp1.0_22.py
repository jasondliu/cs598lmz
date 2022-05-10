import types
# Test types.FunctionType and types.LambdaType.

def f():
    pass

def l():
    pass

assert type(f) == types.FunctionType
assert type(l) == types.FunctionType
assert type(lambda: None) == types.LambdaType

# Test types.GeneratorType.

def g():
    yield 2

assert type(g()) == types.GeneratorType
assert type(x for x in range(10)) == types.GeneratorType

# Test types.MethodType.

class C:
    def m(self):
        pass

assert type(C.m) == types.FunctionType
assert type(C().m) == types.MethodType

# Test types.BuiltinMethodType.

assert type(list.append) == types.BuiltinMethodType
assert type([].append) == types.BuiltinMethodType

# Test types.BuiltinFunctionType.

assert type(min) == types.BuiltinFunctionType

# Test types.ModuleType.

assert type(types) == types.ModuleType

# Test types
