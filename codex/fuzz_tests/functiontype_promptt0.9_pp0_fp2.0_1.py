import types
# Test types.FunctionType
# Test types.LambdaType
@types.FunctionType
def incr(x):
    return x + 1

assert incr(5) == 6

# Test types.UnboundMethodType
# Test types.MethodType
class Eq(int):
    def __eq__(self, other):
        return self.__val__() == other
eq = Eq(3)
assert 3 == eq

# Test types.BuiltinFunctionType
# Test types.BuiltinMethodType
class Y:
    pass

def meth(self):
    return 2

Y.m = types.BuiltinMethodType(meth, None)
x = Y()
assert x.m() == 2

# Test types.ModuleType
# Test types.MappingProxyType
# Test types.DynamicClassAttribute
# Test types.TracebackType
# Test types.FrameType
# Test types.CodeType
a = 3
code = a.__code__
assert isinstance(code, types.CodeType)
# TODO: need to write a better test for this
assert code.co
