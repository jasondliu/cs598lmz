from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo') for _ in range(2))

# Test that the __qualname__ of a function is not set until it is defined
def f():
    pass

assert f.__qualname__ == 'f'

def g():
    f.__qualname__

g()

# Test that the __qualname__ of a function is not set until it is defined
def f():
    pass

assert f.__qualname__ == 'f'

def g():
    f.__qualname__

g()

# Test that the __qualname__ of a function is not set until it is defined
def f():
    pass

assert f.__qualname__ == 'f'

def g():
    f.__qualname__

g()

# Test that the __qualname__ of a function is not set until it is defined
def f():
    pass

assert f.__qualname__ == 'f'

def g():
    f.__qualname__

g()

# Test that the __qualname__
