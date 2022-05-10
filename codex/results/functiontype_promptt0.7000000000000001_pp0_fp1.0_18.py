import types
# Test types.FunctionType type
def foo():
    pass

print(type(foo) == types.FunctionType)
print(type(lambda: None) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# output:
#   True
#   True
#   True

# Test inspect.isgenerator()
import inspect
def foo():
    yield 'foo'

print(inspect.isgenerator(foo()))

# output:
#   True

# Test inspect.isgeneratorfunction()
def foo():
    yield 'foo'

print(inspect.isgeneratorfunction(foo))

# output:
#   True

# Test inspect.isgenerator()
def foo():
    yield 'foo'

foo_gen = foo()
print(inspect.isgenerator(foo_gen))

# output:
#   True

# Test inspect.isgeneratorfunction()
def foo():
    yield 'foo'

print(inspect.isgeneratorfunction(foo))

#
