import types
# Test types.FunctionType

print(types.FunctionType)

print(types.FunctionType.__name__)

print(types.FunctionType.__module__)

print(types.FunctionType.__doc__)

def f(): pass

print(f.__class__)

print(type(f))

print(isinstance(f, types.FunctionType))

try:
    print(types.FunctionType(f))
except TypeError as e:
    print(e)

print(types.FunctionType(f, globals()))

print(types.FunctionType(f.__code__, globals()))

print(types.FunctionType(f.__code__, globals(), "f2"))

print(types.FunctionType(f.__code__, globals(), "f2", (1,2,3)))

print(types.FunctionType(f.__code__, globals(), "f2", (1,2,3), {"x": 1}))

def f2(a,b,c,x=1): pass

print(
