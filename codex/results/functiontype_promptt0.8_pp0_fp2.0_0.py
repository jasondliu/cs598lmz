import types
# Test types.FunctionType

def f(): pass

class C:
    def f(): pass

t = types.FunctionType(f.__code__, {})
t()

t = types.FunctionType(f.__code__, {}, "t")
t()

try:
    t = types.FunctionType(f.__code__, {}, "t", None, None)
    print("should have raised TypeError")
except TypeError:
    pass

import collections

try:
    t = types.FunctionType(f.__code__, dict(a=1))
    print("should have raised TypeError")
except TypeError:
    pass

try:
    t = types.FunctionType(f.__code__, collections.OrderedDict(a=1))
    print("should have raised TypeError")
except TypeError:
    pass

class MyDict(dict):
    def __new__(cls, *args, **kwargs):
        return dict.__new__(cls)

    def __init__(self, *args, **kwargs):
