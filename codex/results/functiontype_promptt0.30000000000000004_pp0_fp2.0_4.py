import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
# Test types.MethodType
class C:
    def m(self):
        pass
assert isinstance(C.m, types.MethodType)
assert isinstance(C().m, types.MethodType)
# Test types.BuiltinMethodType
class C:
    def m(self):
        pass
assert isinstance(C.m, types.BuiltinMethodType)
assert isinstance(C().m, types.BuiltinMethodType)
# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
# Test types.LambdaType
assert isinstance(lambda: None, types.LambdaType)
# Test types.GeneratorType
def f():
    yield
assert isinstance(f(), types.GeneratorType)
# Test types.GeneratorType
def f():
    yield
assert isinstance(f(), types.GeneratorType)
# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)
# Test types.
