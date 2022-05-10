from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo') for _ in range(10))

def f():
    yield
    return

list(f() for _ in range(10))

def f():
    yield
    yield
    return

list(f() for _ in range(10))

def f():
    yield
    yield
    yield
    return

list(f() for _ in range(10))

def f():
    yield
    yield
    yield
    yield
    return

list(f() for _ in range(10))

def f():
    yield
    yield
    yield
    yield
    yield
    return

list(f() for _ in range(10))

def f():
    yield
    yield
    yield
    yield
    yield
    yield
    return

list(f() for _ in range(10))

def f():
    yield
    yield
    yield
    yield
    yield
    yield
    yield
    return

list(f() for _ in range(10))

def f():
   
