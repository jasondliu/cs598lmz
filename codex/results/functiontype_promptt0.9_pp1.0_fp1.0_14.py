import types
# Test types.FunctionType


def a(b):
    pass

assert(types.FunctionType(a.__code__, a.__globals__, a.__name__, a.__defaults__, a.__closure__) == a)

try:
    types.FunctionType(a.__code__, a.__globals__, a.__name__, a.__closure__)
except TypeError:
    pass
else:
    raise Exception("Should not reach here")

try:
    types.FunctionType(a.__code__, a.__globals__, a.__defaults__, a.__closure__)
except TypeError:
    pass
else:
    raise Exception("Should not reach here")

try:
    types.FunctionType(a.__code__, a.__globals__)
except TypeError:
    pass
else:
    raise Exception("Should not reach here")

# Test types.ClassType


class b(object):
    pass

assert (types.ClassType(b.__name__, b.__b
