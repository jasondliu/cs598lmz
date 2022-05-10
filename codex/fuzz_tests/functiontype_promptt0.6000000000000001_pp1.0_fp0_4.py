import types
# Test types.FunctionType
def f1(x):
  return x + 1

assert(type(f1) == types.FunctionType)

# Test types.LambdaType
f2 = lambda x: x + 1

assert(type(f2) == types.LambdaType)

# Test types.GeneratorType
f3 = (x for x in range(10))

assert(type(f3) == types.GeneratorType)
