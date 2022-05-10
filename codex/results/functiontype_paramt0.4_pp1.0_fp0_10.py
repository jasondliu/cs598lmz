from types import FunctionType
list(FunctionType(lambda x: x, globals()) for x in range(3))

# Test that the function object is not kept alive by the generator.
import gc
del x
gc.collect()

# Verify that the function object is not kept alive by the generator.
import gc
gc.collect()

def f():
    yield 1

f().__length_hint__()

def f():
    yield 1
    yield 2

f().__length_hint__()

def f():
    yield 1
    yield 2
    yield 3

f().__length_hint__()

def f():
    yield 1
    yield 2
    yield 3
    yield 4

f().__length_hint__()

def f():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

f().__length_hint__()

def f():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6

f().__length_hint__()

def f():
   
