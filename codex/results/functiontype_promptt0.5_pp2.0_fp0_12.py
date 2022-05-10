import types
# Test types.FunctionType, types.LambdaType, types.BuiltinFunctionType

# Test FunctionType
def f():
    pass
if type(f) != types.FunctionType:
    print('Test failed: type(f) is', type(f))

# Test LambdaType
g = lambda x: x
if type(g) != types.LambdaType:
    print('Test failed: type(g) is', type(g))

# Test BuiltinFunctionType
if type(len) != types.BuiltinFunctionType:
    print('Test failed: type(len) is', type(len))

# Test MethodType
class C:
    def f(self):
        pass
c = C()
if type(c.f) != types.MethodType:
    print('Test failed: type(c.f) is', type(c.f))

# Test UnboundMethodType
if type(C.f) != types.UnboundMethodType:
    print('Test failed: type(C.f) is', type(C.f))

# Test BuiltinMethodType
if
