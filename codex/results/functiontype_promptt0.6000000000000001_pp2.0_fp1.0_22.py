import types
# Test types.FunctionType and types.LambdaType

def f():
    pass

assert isinstance(f, types.FunctionType)
assert not isinstance(f, types.LambdaType)

g = lambda: None

assert isinstance(g, types.FunctionType)
assert isinstance(g, types.LambdaType)

# Test types.GeneratorType

def h():
    yield 42

assert isinstance(h(), types.GeneratorType)

# Test types.BuiltinFunctionType

import math
assert isinstance(math.sin, types.BuiltinFunctionType)

# Test types.BuiltinMethodType

assert isinstance(math.sin, types.BuiltinMethodType)

# Test types.MethodType

class A:
    def f(self):
        pass

a = A()
assert isinstance(a.f, types.MethodType)

# Test types.UnboundMethodType

assert isinstance(A.f, types.UnboundMethodType)
