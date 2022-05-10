import types
# Test types.FunctionType (function objects) and types.MethodType (unbound 
# method objects)

import sys

types.FunctionType
types.MethodType

def f(x): return x

f.__doc__ = 'docstring'
f.__module__ = 'module'
f.__name__ = 'name'

if sys.flags.optimize > 1:
    print "Cannot test function objects in optimized mode"
else:
    assert type(f) is types.FunctionType
    assert f.__name__ == 'name'
    assert f.__doc__ == 'docstring'
    assert f.__module__ == 'module'

assert type(f.__call__) is types.MethodType

# Test bound method objects

>>> class C:
...     def m(self):
...         return 'bound method'

>>> c = C()
>>> assert type(c.m) is types.MethodType
>>> assert c.m() == 'bound method'
>>> assert c.m.__self__ is c
>>> assert c.m.__func__ is c.m
