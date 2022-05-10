import types
# Test types.FunctionType's (unbound) method support:
def f(x, y): return x - y

# This example catches a bug in Python 2.3 where
# method-wrapper objects did not find the method
# operation in the instance's __dict__.

class C(object):
    pass

c = C()
c.f = f

# This should be an unbound method object, not a function
# object:
m = c.f
assert type(m) is types.MethodType

assert m(4, 3) == 1

try:
    m(-5, 2)
except TypeError:
    pass
else:
    raise TestFailed
