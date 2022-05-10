import types
# Test types.FunctionType
def f(): pass
def g(): pass
assert type(f) == types.FunctionType
assert type(g) == types.FunctionType
assert type(f) == type(g)

# Test types.LambdaType
h = lambda: None
assert type(h) == types.LambdaType
assert type(f) != type(h)

# Test types.GeneratorType
def i(): yield
assert type(i()) == types.GeneratorType
assert type(f()) != type(i())

# Test types.CodeType
assert type(f.__code__) == types.CodeType
assert type(g.__code__) == types.CodeType
assert type(f.__code__) == type(g.__code__)

# Test types.MethodType
class A:
    def m(self): pass
assert type(A.m) == types.MethodType
assert type(A().m) == types.MethodType

# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType
assert type(A.m) !=
