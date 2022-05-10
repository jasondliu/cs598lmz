from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo'))

# Test __repr__
def f(): pass
f.__repr__ = lambda: 'repr'
repr(f)

# Test __reduce__
def f(): pass
f.__reduce__ = lambda: 'reduce'
repr(f)

# Test __get__
def f(): pass
f.__get__ = lambda: 'get'
repr(f)

# Test __set__
def f(): pass
f.__set__ = lambda: 'set'
repr(f)

# Test __delete__
def f(): pass
f.__delete__ = lambda: 'delete'
repr(f)

# Test __getattribute__
def f(): pass
f.__getattribute__ = lambda: 'getattribute'
repr(f)

# Test __getattr__
def f(): pass
f.__getattr__ = lambda: 'getattr'
repr(f)

# Test __setattr__
def f(): pass
f.__setattr__ = lambda
