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

# Test __getitem__
def f():
    pass

f.__getitem__(None)

# Test __setitem__
def f():
    pass

f.__setitem__(None, None)

# Test __delitem__
def f():
    pass

f.__delitem__(None)

# Test __lt__
def f():
    pass

f.__lt
