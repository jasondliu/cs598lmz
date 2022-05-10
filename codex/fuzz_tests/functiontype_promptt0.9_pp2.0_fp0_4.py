import types
# Test types.FunctionType
assert(isinstance(max, types.FunctionType))
 
# Test types.GeneratorType
def generate_squares():
	for i in range(10):
		yield i**2

assert(isinstance(generate_squares(), types.GeneratorType))
 
# Test types.LambdaTy
