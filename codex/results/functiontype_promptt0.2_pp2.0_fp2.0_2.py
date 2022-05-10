import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert isinstance(int, types.FunctionType) # metaclass hack

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert isinstance(int, types.BuiltinFunctionType)
assert isinstance(f, types.BuiltinFunctionType) == False

# Test types.MethodType
class C(object):
    def f(self): pass
assert isinstance(C.f, types.MethodType)
assert isinstance(C().f, types.MethodType)

# Test types.UnboundMethodType
assert isinstance(C.f, types.UnboundMethodType) == False
assert isinstance(C().f, types.UnboundMethodType) == False

# Test types.LambdaType
assert isinstance(lambda: None, types.LambdaType)

# Test types.GeneratorType
def g(): yield 1
assert isinstance(g(), types.GeneratorType)

#
