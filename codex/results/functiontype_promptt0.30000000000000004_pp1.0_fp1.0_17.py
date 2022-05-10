import types
# Test types.FunctionType
def f(x):
    return x + 1

assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)

def g(x):
    def h(y):
        return x + y
    return h

assert isinstance(g(1), types.FunctionType)
assert isinstance(g(1), types.BuiltinFunctionType)

def f(x):
    return x + 1

def g(x):
    def h(y):
        return x + y
    return h

assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)
assert isinstance(g(1), types.FunctionType)
assert isinstance(g(1), types.BuiltinFunctionType)

# Test types.MethodType
class A(object):
    def f(self):
        return self.x

a = A()
a.x = 1
assert isinstance(a.f, types.MethodType)
assert isinstance(A.f, types.MethodType)
