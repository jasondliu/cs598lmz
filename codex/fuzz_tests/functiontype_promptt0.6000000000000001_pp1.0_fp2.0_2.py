import types
# Test types.FunctionType
def f(x):
    return x + 1

test(type(f) == types.FunctionType)

# Test types.TypeType
test(type(type(f)) == types.TypeType)

# Test types.LambdaType
test(type(lambda x: x) == types.LambdaType)

# Test types.BuiltinFunctionType
test(type(divmod) == types.BuiltinFunctionType)

# Test types.BuiltinMethodType
test(type("".index) == types.BuiltinMethodType)

# Test types.MethodType
class C:
    def f(self):
        return 42

test(type(C().f) == types.MethodType)

# Test types.UnboundMethodType
test(type(C.f) == types.MethodType)

# Test types.ModuleType
test(type(types) == types.ModuleType)

# Test types.TracebackType
try:
    raise IndexError
except IndexError:
    tb = sys.exc_info()[2]
    test(
