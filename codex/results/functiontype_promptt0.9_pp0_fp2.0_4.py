import types
# Test types.FunctionType
func = lambda: None
assert isinstance(type(1), type)
assert isinstance(1, int)
assert isinstance(func, types.FunctionType)
try:
    isinstance(1, types.FunctionType)
except TypeError:
    pass
else:
    assert False, "expected TypeError"


def raises_value_error(*args, **kwargs):
    raise ValueError

try:
    isinstance(1, raises_value_error)
except ValueError:
    pass
else:
    assert False, "expected ValueError"


class A(object):
    pass

class B(A):
    pass

class C(A):
    pass

assert isinstance(B(), B)
assert isinstance(B(), A)
assert not isinstance(B(), type)
assert isinstance(A(), A)
assert isinstance(C(), A)
assert isinstance(A, type)
assert isinstance(B, type)
assert isinstance(type, type)
assert isinstance(object, type)
assert isinstance(int, type)

