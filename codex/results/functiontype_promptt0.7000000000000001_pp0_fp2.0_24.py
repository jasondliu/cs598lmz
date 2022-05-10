import types
# Test types.FunctionType for function reading.
def foo(a,b,c):
    return a+b+c

# normal function
assert type(foo) == types.FunctionType

# lambda
assert type((lambda: None)) == types.FunctionType
assert type((lambda x: None)) == types.FunctionType
assert type((lambda x,y: None)) == types.FunctionType

# functions in class
class A:
    def f(self, a, b):
        return a+b
    def g(self):
        return 42

assert type(A.f) == types.FunctionType
assert type(A.g) == types.FunctionType

# nested functions
def bar(x):
    def baz(y):
        return x+y
    return baz

assert type(bar) == types.FunctionType
assert type(bar(5)) == types.FunctionType

# instance methods
a = A()
assert type(a.f) == types.MethodType
assert type(a.g) == types.MethodType

# builtins
assert type(abs) == types.
