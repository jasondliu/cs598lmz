import types
# Test types.FunctionType

def f(): pass

assert type(f) is types.FunctionType
assert isinstance(f, types.FunctionType)
assert type(f) == types.FunctionType
assert type(f) != types.BuiltinFunctionType
assert type(f) != types.BuiltinMethodType

# Test types.GeneratorType

def g():
    yield 1

assert type(g()) is types.GeneratorType
assert isinstance(g(), types.GeneratorType)
assert type(g()) == types.GeneratorType
assert type(g()) != types.BuiltinFunctionType
assert type(g()) != types.BuiltinMethodType

# Test types.BuiltinFunctionType

class C:
    def f(self): pass
    def g(self):
        yield 1

assert type(C.f) is types.BuiltinMethodType
assert isinstance(C.f, types.BuiltinMethodType)
assert type(C.f) == types.BuiltinMethodType
assert type(C.f) != types.FunctionType
assert type(C.f) != types.Method
