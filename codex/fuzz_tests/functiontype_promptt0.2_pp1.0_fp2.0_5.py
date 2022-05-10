import types
# Test types.FunctionType
def f():
    pass

assert type(f) is types.FunctionType
assert type(f) is types.BuiltinFunctionType
assert type(f) is types.BuiltinMethodType
assert type(f) is types.MethodType
assert type(f) is types.LambdaType

# Test types.MethodType
class A:
    def f(self):
        pass

assert type(A.f) is types.FunctionType
assert type(A.f) is types.BuiltinFunctionType
assert type(A.f) is types.BuiltinMethodType
assert type(A.f) is types.MethodType
assert type(A.f) is types.LambdaType

# Test types.LambdaType
g = lambda: None
assert type(g) is types.FunctionType
assert type(g) is types.BuiltinFunctionType
assert type(g) is types.BuiltinMethodType
assert type(g) is types.MethodType
assert type(g) is types.LambdaType

# Test types.GeneratorType
def h():
   
