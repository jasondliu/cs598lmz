from types import FunctionType
list(FunctionType(lambda: 0, {}).__code__.co_varnames)

def a():
    return 0

def b():
    return 0

def c():
    return 0

def d():
    return 0

def e():
    return 0

def f():
    return 0

def g():
    return 0

def h():
    return 0

def i():
    return 0

def j():
    return 0

list(FunctionType(a.__code__, {}).__code__.co_varnames) # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
</code>
It seems that the list of "free variables" in the function's code is limited to 10 items.
Is there a way to change this limit ? Or workaround ?

