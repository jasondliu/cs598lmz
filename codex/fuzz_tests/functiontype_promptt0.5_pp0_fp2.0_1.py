import types
# Test types.FunctionType

def f(x):
    return x

def g(x):
    return x

print f.__class__
print type(f)
print types.FunctionType
print type(f) == types.FunctionType
print type(f) == types.FunctionType()

try:
    types.FunctionType(f)
except TypeError, e:
    print e
