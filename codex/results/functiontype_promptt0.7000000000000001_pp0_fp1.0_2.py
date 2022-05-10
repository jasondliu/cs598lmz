import types
# Test types.FunctionType
def foo():
    pass
assert type(foo) == types.FunctionType
# Test types.BuiltinFunctionType
assert type(int) == types.BuiltinFunctionType

# Test types.MethodType
class A(object):
    def foo(self):
        pass

assert type(A.foo) == types.FunctionType
a_foo = A.foo
assert type(a_foo) == types.MethodType
assert type(a_foo.__func__) == types.FunctionType

# Test types.BuiltinMethodType
assert type(int.__add__) == types.BuiltinMethodType
assert type(int.__add__.__func__) == types.BuiltinFunctionType

# Test types.LambdaType
l = lambda: None
assert type(l) == types.LambdaType

# Test types.GeneratorType
def foo():
    for i in range(2):
        yield i
assert type(foo()) == types.GeneratorType

# Test types.CodeType
def foo():
    pass
assert type(foo.__code__
