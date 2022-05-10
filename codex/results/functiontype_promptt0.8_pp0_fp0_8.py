import types
# Test types.FunctionType
def foo(): return True

assert isinstance(types.FunctionType, type)
assert isinstance(foo, types.FunctionType)
assert type(foo) is types.FunctionType

a = 5
assert isinstance(a, int)
assert type(a) is int
assert type(a) == int

# Test object.__dict__

class Bar(object):
    pass

assert hasattr(Bar, '__dict__')
assert hasattr(Bar(), '__dict__')

# Test that you can't set __dict__

try:
    object.__dict__ = 1
except TypeError:
    pass
else:
    raise Exception("Should not be able to set __dict__")

# Test that you can assign delattr

delattr(object, "__dict__")

# Test dict enumeration (order)

d = dict(a=1, b=2, c=3)
d_keys = list(d)
d_vals = list(d.values())
d_items = list(d.items())
# dict has randomized order,
