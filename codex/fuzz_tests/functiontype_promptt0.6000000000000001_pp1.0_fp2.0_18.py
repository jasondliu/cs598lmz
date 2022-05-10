import types
# Test types.FunctionType
assert isinstance(lambda x: x, types.FunctionType)
assert isinstance(lambda x=1: x, types.FunctionType)
assert isinstance(lambda *x: x, types.FunctionType)
assert isinstance(lambda **x: x, types.FunctionType)
assert isinstance(lambda *x, **y: x + y, types.FunctionType)
assert isinstance((lambda x: x).__call__, types.FunctionType)
assert isinstance((lambda x=1: x).__call__, types.FunctionType)
assert isinstance((lambda *x: x).__call__, types.FunctionType)
assert isinstance((lambda **x: x).__call__, types.FunctionType)
assert isinstance((lambda *x, **y: x + y).__call__, types.FunctionType)

# Test types.LambdaType
assert isinstance(lambda x: x, types.LambdaType)
assert isinstance(lambda x=1: x, types.LambdaType)
assert isinstance(lambda *x: x, types.LambdaType)

