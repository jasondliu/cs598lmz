import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)

# Test types.LambdaType
l = lambda: None
assert isinstance(l, types.LambdaType)

# Test types.GeneratorType
g = (i for i in range(5))
assert isinstance(g, types.GeneratorType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
assert isinstance([].append, types.BuiltinMethodType)

# Test types.MethodType
class A:
    def __init__(self):
        self.x = 1
    def get_x(self):
        return self.x
    def set_x(self, x):
        self.x = x

a = A()
assert isinstance(a.get_x, types.MethodType)
assert isinstance(a.set_x, types.MethodType)

# Test types.UnboundMethodType
assert isinstance(A.get_x, types.Un
