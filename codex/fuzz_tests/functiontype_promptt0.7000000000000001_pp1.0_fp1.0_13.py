import types
# Test types.FunctionType

def f():
    pass

def g(x):
    return x

def h():
    return 42

def i(x, y):
    return x, y

print types.FunctionType
print type(f) == types.FunctionType
print type(g) == types.FunctionType
print type(h) == types.FunctionType
print type(i) == types.FunctionType

class A:
    def a(self):
        pass
    def b(self, x):
        return x
    def c(self):
        return 42
    def d(self, x, y):
        return x, y

print type(A.a) == types.FunctionType
print type(A.b) == types.FunctionType
print type(A.c) == types.FunctionType
print type(A.d) == types.FunctionType
