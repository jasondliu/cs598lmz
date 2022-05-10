from types import FunctionType
list(FunctionType(f.__code__, globals(), 'name'))
f.__code__.co_varnames
f.__code__.co_argcount

def counter(initial_value=0):
    def inc(increment=1):
        nonlocal initial_value
        initial_value += increment
        return initial_value
    return inc

c1 = counter()
c2 = counter(100)
c1(), c1(10), c1(), c2()

def factorial(n):
    """Return n!"""
    return 1 if n < 2 else n * factorial(n-1)

factorial(5), factorial.__doc__


# mutable default arguments
def f(a, L=[]):
    L.append(a)
    return L

f(1), f(2), f(3), f(1, ['a','b','c']), f(1)

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
f(1
