import types
# Test types.FunctionType
def f():
    pass

def g():
    pass

assert type(f) == types.FunctionType
assert type(g) == types.FunctionType
assert f != g

# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType
assert type(int) == types.BuiltinFunctionType
assert type(len) != type(int)

# Test types.BuiltinMethodType
assert type([].append) == types.BuiltinMethodType
assert type([].count) == types.BuiltinMethodType
assert type([].append) != type([].count)

# Test types.MethodType
class C:
    def f(self):
        pass

c = C()
assert type(c.f) == types.MethodType
assert type(C.f) == types.FunctionType
assert type(c.f) != type(C.f)

# Test types.LambdaType
assert type(lambda: None) == types.LambdaType

# Test types.GeneratorType
def gen():
    yield 1

assert
