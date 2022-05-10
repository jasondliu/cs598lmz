import types
# Test types.FunctionType
def f():
    pass

def g():
    pass

assert type(f) == types.FunctionType
assert type(g) == types.FunctionType
assert type(f) == type(g)
assert type(f) != int
assert type(f) != type(1)
assert type(f) != type(lambda: None)

# Test types.LambdaType
assert type(lambda: None) == types.LambdaType
assert type(lambda: None) != types.FunctionType
assert type(lambda: None) != type(f)
assert type(lambda: None) != type(g)

# Test types.MethodType
class A:
    def f(self):
        pass

assert type(A.f) == types.MethodType
assert type(A.f) != types.FunctionType
assert type(A.f) != type(f)
assert type(A.f) != type(g)

# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType
assert type(len) != types.FunctionType

