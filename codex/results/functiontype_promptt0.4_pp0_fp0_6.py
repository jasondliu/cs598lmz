import types
# Test types.FunctionType
def f():
    pass

def g():
    pass

assert type(f) == types.FunctionType
assert type(g) == types.FunctionType
assert type(f) == type(g)
# Test types.MethodType
class A:
    def f(self):
        pass

a = A()
assert type(a.f) == types.MethodType
assert type(A.f) == types.FunctionType
# Test types.BuiltinMethodType
class B:
    def f(self):
        pass

b = B()
assert type(b.__str__) == types.BuiltinMethodType
assert type(B.__str__) == types.BuiltinMethodType
# Test types.BuiltinFunctionType
assert type(str) == types.BuiltinFunctionType
# Test types.LambdaType
assert type(lambda: None) == types.LambdaType
# Test types.GeneratorType
assert type((x for x in range(10))) == types.GeneratorType
# Test types.CodeType
assert type(f.__code__) ==
