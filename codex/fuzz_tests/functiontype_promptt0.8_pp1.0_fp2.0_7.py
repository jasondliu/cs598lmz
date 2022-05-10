import types
# Test types.FunctionType for sanity's sake
assert type(lambda x: x) == types.FunctionType
# Test types.LambdaType for sanity's sake
assert type(lambda x: x) == types.LambdaType 

def f((x,y)):
    return x+y
# Test types.TupleType for sanity's sake
assert type(f) == types.FunctionType
# Test types.LambdaType for sanity's sake
assert type(lambda x: x) == types.LambdaType 

# Test types.FunctionType for sanity's sake
assert type(lambda x: x) == types.FunctionType
# Test types.LambdaType for sanity's sake
assert type(lambda x: x) == types.LambdaType 

# Test types.FunctionType for sanity's sake
assert type(lambda x: x) == types.FunctionType
# Test types.LambdaType for sanity's sake
assert type(lambda x: x) == types.LambdaType 

def g(x,y,z):
    return x+y+z

def f(x,
