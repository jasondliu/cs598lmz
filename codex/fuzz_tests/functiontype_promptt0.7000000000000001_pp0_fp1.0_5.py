import types
# Test types.FunctionType
# See http://docs.python.org/library/types.html#types.FunctionType

def f():
    pass

def g(x):
    return x

class C:
    def m(self):
        pass

assert isinstance(f, types.FunctionType)
assert isinstance(g, types.FunctionType)
assert isinstance(C.m, types.FunctionType)
# Test types.LambdaType
# See http://docs.python.org/library/types.html#types.LambdaType

# TODO: add tests when implemented

print('passed all tests...')
