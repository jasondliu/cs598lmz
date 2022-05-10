from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo'))

# Test __repr__
def f():
    pass

f.__repr__ = lambda: 'foo'
repr(f)

# Test __str__
def f():
    pass

f.__str__ = lambda: 'foo'
str(f)

# Test __get__
def f():
    pass

f.__get__ = lambda: 'foo'
f.__get__()

# Test __set__
def f():
    pass

f.__set__ = lambda: 'foo'
f.__set__()

# Test __delete__
def f():
    pass

f.__delete__ = lambda: 'foo'
f.__delete__()

# Test __call__
def f():
    pass

f.__call__ = lambda: 'foo'
f()

# Test __getitem__
def f():
    pass

f.__getitem__ = lambda: 'foo'
f[0]

# Test __setitem__
def f
