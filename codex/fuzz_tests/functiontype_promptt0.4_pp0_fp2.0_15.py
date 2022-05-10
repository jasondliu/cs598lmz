import types
# Test types.FunctionType()
class A:
    def f(self):
        pass

a = A()
assert type(a.f) == types.MethodType
assert type(A.f) == types.FunctionType

def f():
    pass
assert type(f) == types.FunctionType

class B:
    pass
assert type(B.__init__) == types.FunctionType

# Test types.LambdaType()
l = lambda: None
assert type(l) == types.LambdaType

# Test types.GeneratorType()
def g():
    yield 1

assert type(g()) == types.GeneratorType

# Test types.CodeType()
def h():
    pass
assert type(h.__code__) == types.CodeType

# Test types.BuiltinFunctionType()
assert type(len) == types.BuiltinFunctionType
assert type(list.append) == types.BuiltinMethodType

# Test types.MethodDescriptorType()
assert type(list.__dict__['append']) == types.MethodDescriptorType


