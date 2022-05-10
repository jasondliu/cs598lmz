import types
# Test types.FunctionType
def f(x):
	return
assert type(f) == types.FunctionType, 'function is not of type FunctionType'

# Test types.GeneratorType
def gen1():
	for i in range(1,10):
		yield i
assert type(gen1) == types.FunctionType, 'function is not of type FunctionType'
assert type(gen1()) == types.GeneratorType, 'generator is not of type GeneratorType'

# Test types.TypeType
# Note: PyPy python has types.TypeType = type which makes it an intance
# of itself, making testing a bit tough
if type(type) is types.TypeType:
	assert type(type) == types.TypeType, 'type is not of type TypeType'
