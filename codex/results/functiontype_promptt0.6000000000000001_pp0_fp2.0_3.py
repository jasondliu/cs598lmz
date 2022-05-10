import types
# Test types.FunctionType
def foo(): pass
assert isinstance(foo, types.FunctionType)
assert type(foo) is types.FunctionType

# Test types.BuiltinFunctionType
assert isinstance(type, types.BuiltinFunctionType)
assert type(type) is types.BuiltinFunctionType

# Test types.BuiltinMethodType
assert isinstance([].append, types.BuiltinMethodType)
assert type([].append) is types.BuiltinMethodType

# Test types.MethodType
class A:
    def foo(self): pass
assert isinstance(A().foo, types.MethodType)
assert type(A().foo) is types.MethodType

# Test types.UnboundMethodType
assert isinstance(A.foo, types.UnboundMethodType)
assert type(A.foo) is types.UnboundMethodType

# Test types.LambdaType
assert isinstance(lambda: None, types.LambdaType)
assert type(lambda: None) is types.LambdaType

# Test types.GeneratorType
assert isinstance((x for x in []), types.
