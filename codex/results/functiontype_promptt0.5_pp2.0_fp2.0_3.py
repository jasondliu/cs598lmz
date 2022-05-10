import types
# Test types.FunctionType
def f(x): return x*x
assert isinstance(f, types.FunctionType)
assert hasattr(f, '__code__')
assert hasattr(f, '__globals__')
assert hasattr(f, '__name__')
assert hasattr(f, '__defaults__')
assert hasattr(f, '__kwdefaults__')
assert hasattr(f, '__closure__')
assert hasattr(f, '__annotations__')
assert hasattr(f, '__dict__')
assert hasattr(f, '__module__')
assert hasattr(f, '__qualname__')
assert hasattr(f, '__get__')
assert hasattr(f, '__call__')
assert hasattr(f, '__text_signature__')
assert hasattr(f, '__doc__')
assert hasattr(f, '__defaults__')
assert hasattr(f, '__kwdefaults__')
assert hasattr(f, '__code__')
assert hasattr(f, '__closure__')
assert hasattr
