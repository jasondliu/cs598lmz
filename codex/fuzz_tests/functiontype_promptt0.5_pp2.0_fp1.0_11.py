import types
# Test types.FunctionType
def f(x): return x
assert type(f) == types.FunctionType
assert type(lambda x: x) == types.FunctionType
assert type(lambda x=1: x) == types.FunctionType
assert type(lambda *args: args) == types.FunctionType
assert type(lambda **kwargs: kwargs) == types.FunctionType
assert type(lambda *args, **kwargs: args) == types.FunctionType
assert type(lambda *args, **kwargs: kwargs) == types.FunctionType
assert type(lambda *args, **kwargs: (args, kwargs)) == types.FunctionType

# Test types.LambdaType
assert type(lambda x: x) == types.LambdaType
assert type(lambda x=1: x) == types.LambdaType
assert type(lambda *args: args) == types.LambdaType
assert type(lambda **kwargs: kwargs) == types.LambdaType
assert type(lambda *args, **kwargs: args) == types.LambdaType
assert type(lambda *args
