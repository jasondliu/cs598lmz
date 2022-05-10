import types
# Test types.FunctionType for alias compatibility

def f(): pass

# First test an empty list
types.FunctionType.__bases__ = ()
f.__mro__

try:
    exec('def g(): pass', {'__bases__': ()})
except TypeError:
    print('SKIP')
    raise SystemExit

class C: pass
C.__bases__ = types.FunctionType,

# Instances of builtin types cannot be subclassed
# FunctionType does not have a __new__
try:
    class D(types.FunctionType): pass
except TypeError:
    print('SKIP')
    raise SystemExit

print('OK')
