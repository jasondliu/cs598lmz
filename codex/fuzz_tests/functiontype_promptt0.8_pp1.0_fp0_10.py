import types
# Test types.FunctionType

def foo(): pass
def bar(): pass

def baz():
    return foo()

assert isinstance(foo, types.FunctionType)
assert isinstance(bar, types.FunctionType)
assert isinstance(baz, types.FunctionType)

# Test types.BuiltinFunctionType

assert isinstance(int, types.BuiltinFunctionType)
assert isinstance(type, types.BuiltinFunctionType)
assert isinstance(len, types.BuiltinFunctionType)
assert isinstance(min, types.BuiltinFunctionType)
assert isinstance(max, types.BuiltinFunctionType)

# Test types.BuiltinMethodType

assert isinstance(b'bytes'.upper, types.BuiltinMethodType)
assert isinstance([1,2].append, types.BuiltinMethodType)
assert isinstance(set('abc').union, types.BuiltinMethodType)
assert isinstance({'foo': 'bar'}.setdefault, types.BuiltinMethodType)
assert isinstance(type(42).__init__, types.BuiltinMethodType)

# Test types.Un
