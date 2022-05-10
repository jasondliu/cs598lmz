import types
# Test types.FunctionType
# Create a function
def test(a, b, c):
    return a, b, c

# Create a function type
func = types.FunctionType(test.__code__, test.__globals__, name=test.__name__,
                          argdefs=test.__defaults__,
                          closure=test.__closure__)

# test
assert test == func
assert test(1, 2, 3) == func(1, 2, 3)

# Test types.GeneratorType
# Create a generator
def gen(a, b, c):
    for item in a:
        yield item
        yield b
        yield c

# Create a closure
wrapper = gen.__closure__[0]

# Variable created within gen, we can use the globals from the function
# to get the outputs from getitem.
arg = gen.__globals__["__builtins__"]["range"]

# Create a generator type
gen_type = types.GeneratorType(gen.__code__, gen.__globals__, name=gen
