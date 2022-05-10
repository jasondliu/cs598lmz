from types import FunctionType
list(FunctionType(f.__code__,globals(),'f'))

def f():
    yield 1
    yield 2
    return 'done'
f()
f().__next__()
f().__next__()
f().__next__()

def f():
    yield 1
    yield 2
    return 'done'
f()
f().__next__()
f().__next__()
f().__next__()
f().__next__()

def f():
    yield 1
    yield 2
    return 'done'
f()
f().__next__()
f().__next__()
f().__next__()
f().__next__()

def f():
    yield 1
    yield 2
    return 'done'
f()
f().__next__()
f().__next__()
f().__next__()
f().__next__()

def f():
    yield 1
    yield 2
    return 'done'
f()
f().__next__()
f().__next__()
f().__next__()
f().__next
