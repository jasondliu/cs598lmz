import types
# Test types.FunctionType, but not too many.

def f():
    pass
f2 = f

def g():
    pass

print(type(f) == type(f2) == type(g) == types.FunctionType)
print(type(f) == types.BuiltinFunctionType)
print(isinstance(f, types.BuiltinFunctionType))
print(isinstance(f, types.FunctionType))

import sys
print(isinstance(f, sys.addaudithook))

import builtins
print(isinstance(f, builtins.print))
print(isinstance(f, builtins.vars))
print(isinstance(f, builtins.len))
print(f in builtins.vars())
print(f in builtins.vars().values())
print(f in builtins.vars().values() + [builtins.print, builtins.vars, builtins.len])

# Import 5 builtin types again
l = [str, bytes, bytearray, memoryview, type]
s = enumerate(l)
d = dict(s
