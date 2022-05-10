from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo'))

# Test __repr__
def f():
    pass

f.__repr__()

# Test __str__
def f():
    pass

f.__str__()

# Test __get__
def f():
    pass

f.__get__(None, None)

# Test __set__
def f():
    pass

f.__set__(None, None)

# Test __delete__
def f():
    pass

f.__delete__(None)

# Test __call__
def f():
    pass

f.__call__()

# Test __code__
def f():
    pass

f.__code__

# Test __defaults__
def f():
    pass

f.__defaults__

# Test __globals__
def f():
    pass

f.__globals__

# Test __closure__
def f():
    pass

f.__closure__

# Test __annotations__
def
