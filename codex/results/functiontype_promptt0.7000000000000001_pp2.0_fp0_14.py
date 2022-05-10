import types
# Test types.FunctionType

# The type of a function is types.FunctionType
assert type(lambda x: x) == types.FunctionType
# The type of a method is types.MethodType
class A:
    def f(self):
        pass
assert type(A.f) == types.MethodType

# A function is not a method
def f():
    pass
assert not isinstance(f, types.MethodType)
# A method is not a function
class B:
    def g(self):
        pass
assert not isinstance(B.g, types.FunctionType)
# Test types.LambdaType

# The type of a lambda is types.LambdaType
assert type(lambda x: x) == types.LambdaType
# Test types.GeneratorType

# The type of a generator is types.GeneratorType
def g(n):
    yield from range(n)
assert type(g(10)) == types.GeneratorType
# Test types.GeneratorType with a for loop

# The type of a for loop is types.GeneratorType
total = 0
for
