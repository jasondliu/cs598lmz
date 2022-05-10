import types
# Test types.FunctionType
def f():
    pass

assert type(f) == types.FunctionType
assert type(f) == types.BuiltinFunctionType

# Test types.MethodType
class C:
    def m(self):
        pass

assert type(C.m) == types.MethodType
assert type(C.m) == types.BuiltinMethodType

# Test types.LambdaType
l = lambda: None
assert type(l) == types.LambdaType
assert type(l) == types.FunctionType

# Test types.GeneratorType
def g():
    yield 1

assert type(g()) == types.GeneratorType
assert type(g()) == types.BuiltinFunctionType

# Test types.CodeType
assert type(f.__code__) == types.CodeType
assert type(l.__code__) == types.CodeType
assert type(g.__code__) == types.CodeType
assert type(C.m.__code__) == types.CodeType

# Test types.TracebackType
try:
    raise Exception
except
