import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)

# Test types.BuiltinFunctionType
assert isinstance(abs, types.BuiltinFunctionType)

# Test types.MethodType
class A:
    def f(self): pass
assert isinstance(A.f, types.MethodType)

# Test types.UnboundMethodType
assert isinstance(A.f.__get__(A()), types.MethodType)
assert isinstance(A.f.__get__(A()), types.MethodType)

# Test types.BuiltinMethodType
assert isinstance(A.__new__, types.BuiltinMethodType)

# Test types.LambdaType
assert isinstance(lambda: None, types.LambdaType)

# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)

# Test types.TracebackType
try:
    raise Exception
except:
    import sys
    assert isinstance(sys.exc_info()[2], types.TracebackType)

# Test
