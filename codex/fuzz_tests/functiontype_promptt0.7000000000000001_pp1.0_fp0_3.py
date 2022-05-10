import types
# Test types.FunctionType
assert isinstance(lambda x: x, types.FunctionType)

# Test types.LambdaType
assert isinstance(lambda x: True, types.LambdaType)
# Test types.GeneratorType
def gen():
    yield 1
assert isinstance(gen(), types.GeneratorType)

# Test isinstance(<class>, (type1,type2))
class A(object):
    pass

assert isinstance(A(), (type, object))

# Test isinstance(<class>, (type1,))
assert isinstance(A(), (type,))

# Test isinstance(<class instance>, (type1,type2))
assert isinstance(A(), (object,type))

# Test isinstance(<class instance>, (type1,))
assert isinstance(A(), (type,))

# Test isinstance(<anonymous class instance>, (type1,type2))
assert isinstance(A(), (object,type))

# Test isinstance(<anonymous class instance>, (type1,))
assert isinstance(A(), (type,))

