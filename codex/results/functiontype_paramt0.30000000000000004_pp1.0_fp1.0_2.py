from types import FunctionType
list(FunctionType(lambda: None, globals()) for i in range(10))

# Test that the __code__ object is correctly created.
def f():
    pass

def g():
    pass

def h():
    pass

f.__code__ = g.__code__
f.__code__ = h.__code__

# Test that the __code__ object is correctly created.
def f():
    pass

def g():
    pass

def h():
    pass

f.__code__ = g.__code__
f.__code__ = h.__code__

# Test that the __code__ object is correctly created.
def f():
    pass

def g():
    pass

def h():
    pass

f.__code__ = g.__code__
f.__code__ = h.__code__

# Test that the __code__ object is correctly created.
def f():
    pass

def g():
    pass

def h():
    pass

f.__code__ = g.__code__
f.__code
