from types import FunctionType
list(FunctionType(lambda x: x+1, globals(), 'foo')(1))

# Test __globals__
def f():
    return __globals__

f.__globals__ == globals()

# Test __code__
def f():
    return __code__

f.__code__ == f.__code__

# Test __defaults__
def f(a, b=1, c=2):
    return __defaults__

f.__defaults__ == (1, 2)

# Test __kwdefaults__
def f(a, b=1, c=2, *, d=3, e=4):
    return __kwdefaults__

f.__kwdefaults__ == {'d': 3, 'e': 4}

# Test __annotations__
def f(a: 1, b: 2, c: 3):
    return __annotations__

f.__annotations__ == {'a': 1, 'b': 2, 'c': 3}

# Test __closure__
def f():
    x
