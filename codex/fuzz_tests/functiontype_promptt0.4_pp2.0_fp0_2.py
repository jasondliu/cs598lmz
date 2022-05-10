import types
# Test types.FunctionType

def func():
    pass

assert isinstance(func, types.FunctionType)
assert isinstance(func, types.BuiltinFunctionType)
assert not isinstance(func, types.BuiltinMethodType)
assert not isinstance(func, types.MethodType)

class A:
    def func(self):
        pass

assert not isinstance(A.func, types.FunctionType)
assert not isinstance(A.func, types.BuiltinFunctionType)
assert not isinstance(A.func, types.BuiltinMethodType)
assert isinstance(A.func, types.MethodType)

assert isinstance(A().func, types.FunctionType)
assert not isinstance(A().func, types.BuiltinFunctionType)
assert not isinstance(A().func, types.BuiltinMethodType)
assert not isinstance(A().func, types.MethodType)

class B:
    def func(self):
        pass
    def __init__(self):
        self.func = func

assert isinstance(B().func, types.FunctionType)
assert is
