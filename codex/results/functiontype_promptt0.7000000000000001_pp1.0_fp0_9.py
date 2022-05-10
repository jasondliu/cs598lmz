import types
# Test types.FunctionType
def foo():
    pass

assert isinstance(foo, types.FunctionType)
assert not isinstance(foo, types.BuiltinFunctionType)
# Test types.BuiltinFunctionType
assert isinstance(hex, types.BuiltinFunctionType)
assert not isinstance(hex, types.FunctionType)
 
# Test types.MethodType
class C:
    def foo(self):
        pass

assert isinstance(C().foo, types.MethodType)
# Test types.UnboundMethodType
assert isinstance(C.foo, types.UnboundMethodType)
# Test types.LambdaType
assert isinstance(lambda x: x, types.LambdaType)
# Test types.GeneratorType
assert isinstance((x for x in range(10)), types.GeneratorType)
# Test types.CodeType
assert isinstance(C.foo.__code__, types.CodeType)
# Test types.TracebackType
try:
    1 / 0
except ZeroDivisionError:
    import sys
    tb = sys.exc_info()[2]

