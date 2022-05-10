import types
# Test types.FunctionType
try:
    f = types.FunctionType(None, None)
except TypeError:
    pass
else:
    raise TestFailed, "FunctionType(None, None) should have failed"

# Test types.MethodType
def f():
    pass
try:
    m = types.MethodType(f, None)
except TypeError:
    pass
else:
    raise TestFailed, "MethodType(f, None) should have failed"

# Test types.BuiltinFunctionType
try:
    b = types.BuiltinFunctionType(f)
except TypeError:
    pass
else:
    raise TestFailed, "BuiltinFunctionType(f) should have failed"

# Test types.BuiltinMethodType
try:
    b = types.BuiltinMethodType(f)
except TypeError:
    pass
else:
    raise TestFailed, "BuiltinMethodType(f) should have failed"

# Test types.GeneratorType
def g():
    yield 1
try:
    gt = types.GeneratorType(g)
except Type
