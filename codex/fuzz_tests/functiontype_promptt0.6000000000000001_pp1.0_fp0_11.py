import types
# Test types.FunctionType
try:
    types.FunctionType
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test builtin methods
def f():
    pass

print(type(f.__code__) == types.CodeType)
print(type(f.__globals__) == types.DictProxyType)
print(type(f.__closure__) == types.TupleType)
print(type(f.__defaults__) == types.TupleType)
print(type(f.__name__) == str)
print(type(f.__qualname__) == str)

# Test that __code__ can be set
def g():
    pass

g.__code__ = f.__code__
print(g())
