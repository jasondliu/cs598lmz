from types import FunctionType
list(FunctionType(lambda: None, globals(), 'lambda'))

# Test that the __name__ attribute of a function is set correctly.
def f(): pass
f.__name__

# Test that the __name__ attribute of a function is writable.
def f(): pass
f.__name__ = 'g'
f.__name__

# Test that the __name__ attribute of a function is writable.
def f(): pass
f.__name__ = 'g'
f.__name__

# Test that the __name__ attribute of a function is writable.
def f(): pass
f.__name__ = 'g'
f.__name__

# Test that the __name__ attribute of a function is writable.
def f(): pass
f.__name__ = 'g'
f.__name__

# Test that the __name__ attribute of a function is writable.
def f(): pass
f.__name__ = 'g'
f.__name__

# Test that the __name__ attribute of a function is writable.
def f(): pass
f.__
