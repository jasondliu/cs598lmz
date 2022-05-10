import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)
assert isinstance(f, types.BuiltinMethodType)

assert not isinstance(f, types.MethodType)
assert not isinstance(f, types.UnboundMethodType)

class C:
    def f():
        pass

assert isinstance(C.f, types.FunctionType)
assert isinstance(C.f, types.MethodType)
assert isinstance(C.f, types.UnboundMethodType)

assert not isinstance(C.f, types.BuiltinFunctionType)
assert not isinstance(C.f, types.BuiltinMethodType)

# Test types.MethodType
class C:
    def f(self):
        pass

c = C()
assert isinstance(c.f, types.MethodType)
assert isinstance(c.f, types.BuiltinMethodType)

assert not isinstance(c.f, types.FunctionType)
assert not isinstance(c.f, types
