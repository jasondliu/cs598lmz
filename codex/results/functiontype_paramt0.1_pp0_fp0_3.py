from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo'))

# Test that the __name__ attribute is set correctly
def f(): pass
f.__name__

# Test that the __doc__ attribute is set correctly
def f(): pass
f.__doc__

# Test that the __dict__ attribute is set correctly
def f(): pass
f.__dict__

# Test that the __module__ attribute is set correctly
def f(): pass
f.__module__

# Test that the __defaults__ attribute is set correctly
def f(a=1): pass
f.__defaults__

# Test that the __code__ attribute is set correctly
def f(): pass
f.__code__

# Test that the __closure__ attribute is set correctly
def f(): pass
f.__closure__

# Test that the __globals__ attribute is set correctly
def f(): pass
f.__globals__

# Test that the __dict__ attribute is set correctly
def f(): pass
f.__dict__

# Test that the __name__ attribute is set correctly
def f(): pass
