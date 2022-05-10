import types
# Test types.FunctionType
assert isinstance(lambda x: x, types.FunctionType)
assert isinstance(map, types.BuiltinFunctionType)

# Test types.LambdaType
assert isinstance(lambda x: x, types.LambdaType)
assert isinstance(map, types.BuiltinFunctionType)

def f(x):
    return x

def f2(x):
    def g(y):
        return y
    return g

# Test types.UnboundMethodType
assert isinstance(f.__call__, types.UnboundMethodType)
assert isinstance(f2.__call__, types.UnboundMethodType)

class C:
    def method(self, x):
        return x

# Test types.MethodType
assert isinstance(C.method, types.MethodType)
assert isinstance(C().method, types.MethodType)

# Test types.BuiltinMethodType
assert isinstance(C.__call__, types.BuiltinMethodType)
assert isinstance(C().__call__, types.BuiltinMethodType)

# Test
