from types import FunctionType
list(FunctionType(lambda: None, {}, 'foo') for _ in range(10))

def foo():
    for _ in range(10):
        yield None
list(FunctionType(foo, {}, 'foo') for _ in range(10))

def foo():
    for _ in range(10):
        yield None
list(FunctionType(foo, {}, 'foo'))

def foo():
    for _ in range(10):
        yield None
list(FunctionType(foo, {}))

def foo():
    for _ in range(10):
        yield None
list(FunctionType(foo))

def foo():
    for _ in range(10):
        yield None
list(FunctionType(foo, {}, 'foo') for _ in range(10))

def foo():
    for _ in range(10):
        yield None
list(FunctionType(foo, {}, 'foo'))

def foo():
    for _ in range(10):
        yield None
list(FunctionType(foo, {}))

def foo():
    for _ in range(10):
        yield
