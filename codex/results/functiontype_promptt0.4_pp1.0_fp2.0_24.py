import types
# Test types.FunctionType
try:
    types.FunctionType
except AttributeError:
    print("SKIP")
    raise SystemExit

def f():
    pass

assert isinstance(f, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.MethodType)
assert not isinstance(f, types.BuiltinMethodType)

# Test types.BuiltinFunctionType
try:
    types.BuiltinFunctionType
except AttributeError:
    print("SKIP")
    raise SystemExit

assert isinstance(abs, types.BuiltinFunctionType)
assert not isinstance(abs, types.FunctionType)
assert not isinstance(abs, types.MethodType)
assert not isinstance(abs, types.BuiltinMethodType)

# Test types.MethodType
try:
    types.MethodType
except AttributeError:
    print("SKIP")
    raise SystemExit

class C:
    def m(self):
        pass

assert isinstance(C.m, types.MethodType)
assert not is
