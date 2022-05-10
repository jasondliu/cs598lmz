from types import FunctionType
list(FunctionType(f, g)(3))

# Example 6.16
def N():
    return lambda x: x+2
def S():
    return lambda x: x-2
def increment(n):
    return N()(n)
def decrement(n):
    return S()(n)
type(increment), type(decrement)

# Example 6.17
f = lambda x: lambda y: (x+1)*(y+2)
a, type(a) = f(3)
b, type(b) = a(5)
b, type(b)
a(5)
f(3)(5)

# Example 6.18
def a():
    return lambda x: lambda y: x*(y+2)
f = a()
f(5)
f(5)(2)

# Example 6.19
def curry(f):
    return lambda x: lambda y: f(x,y)

def f(x,y):
    return (x-1)*(y-2)
h = curry(f)
h(2)(
