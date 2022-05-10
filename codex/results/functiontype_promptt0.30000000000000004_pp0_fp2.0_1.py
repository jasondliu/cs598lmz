import types
# Test types.FunctionType
def f():
    pass

def g():
    pass

def h():
    pass

print(type(f))
print(type(g))
print(type(h))

print(type(f) == types.FunctionType)
print(type(g) == types.FunctionType)
print(type(h) == types.FunctionType)

print(type(f) == type(g))
print(type(f) == type(h))
print(type(g) == type(h))

print(type(f) == types.BuiltinFunctionType)
print(type(g) == types.BuiltinFunctionType)
print(type(h) == types.BuiltinFunctionType)

print(type(f) == types.MethodType)
print(type(g) == types.MethodType)
print(type(h) == types.MethodType)

print(type(f) == types.BuiltinMethodType)
print(type(g) == types.BuiltinMethodType)
print(type(h) == types.BuiltinMethodType)

