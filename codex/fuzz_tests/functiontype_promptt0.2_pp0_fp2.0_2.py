import types
# Test types.FunctionType
def f():
    pass
assert type(f) == types.FunctionType
assert type(f) == types.BuiltinFunctionType
# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType
assert type(len) == types.FunctionType
# Test types.MethodType
class A:
    def f(self):
        pass
assert type(A.f) == types.MethodType
# Test types.UnboundMethodType
assert type(A.f) == types.MethodType
assert type(A.f) == types.UnboundMethodType
# Test types.LambdaType
assert type(lambda x: x) == types.LambdaType
# Test types.GeneratorType
assert type((x for x in range(10))) == types.GeneratorType
# Test types.CodeType
assert type(f.__code__) == types.CodeType
# Test types.TracebackType
try:
    1/0
except:
    import sys
    tb = sys.exc_info()[2]
    assert type(tb) ==
