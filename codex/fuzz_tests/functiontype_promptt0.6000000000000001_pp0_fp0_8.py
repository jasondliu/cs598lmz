import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
# Test types.LambdaType
l = lambda: None
assert isinstance(l, types.LambdaType)
# Test types.GeneratorType
g = (x for x in range(5))
assert isinstance(g, types.GeneratorType)
# Test types.CodeType
def f():
    pass
assert isinstance(f.__code__, types.CodeType)
# Test types.UnboundMethodType
class C:
    def f(self):
        pass
assert isinstance(C.f, types.UnboundMethodType)
# Test types.MethodType
class C:
    def f(self):
        pass
assert isinstance(C().f, types.MethodType)
# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
# Test types.BuiltinMethodType
assert isinstance([].append, types.BuiltinMethodType)
# Test types.ModuleType
assert isinstance(types, types.ModuleType)
# Test types
