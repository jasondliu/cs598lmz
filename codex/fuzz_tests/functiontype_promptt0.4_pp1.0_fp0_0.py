import types
# Test types.FunctionType
def f():
    pass
assert type(f) is types.FunctionType
assert isinstance(f, types.FunctionType)

# Test types.LambdaType
l = lambda: None
assert type(l) is types.LambdaType
assert isinstance(l, types.LambdaType)

# Test types.GeneratorType
g = (i for i in range(10))
assert type(g) is types.GeneratorType
assert isinstance(g, types.GeneratorType)

# Test types.MethodType
class Foo:
    def bar(self):
        pass
assert type(Foo.bar) is types.MethodType
assert isinstance(Foo.bar, types.MethodType)

# Test types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
assert type([].append) is types.BuiltinMethodType
assert isinstance([].append, types.BuiltinMethodType)

# Test types.ModuleType

