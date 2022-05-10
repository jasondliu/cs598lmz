import types
# Test types.FunctionType

def f(): pass
def g(a): pass
def h(a, b): pass
def k(a, b, c=1, d=2): pass

assert isinstance(f, types.FunctionType)
assert isinstance(g, types.FunctionType)
assert isinstance(h, types.FunctionType)
assert isinstance(k, types.FunctionType)

assert isinstance(lambda: None, types.FunctionType)
assert isinstance(lambda x: None, types.FunctionType)
assert isinstance(lambda x, y: None, types.FunctionType)
assert isinstance(lambda x, y, z=1: None, types.FunctionType)

# Test types.BuiltinFunctionType

assert isinstance(abs, types.BuiltinFunctionType)
assert isinstance(chr, types.BuiltinFunctionType)
assert isinstance(dir, types.BuiltinFunctionType)
assert isinstance(divmod, types.BuiltinFunctionType)
assert isinstance(eval, types.BuiltinFunctionType)
assert isinstance(exec, types.BuiltinFunctionType)
assert
