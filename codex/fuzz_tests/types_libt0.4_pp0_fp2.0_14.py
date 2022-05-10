import types
types.MethodType(lambda self, x: x, None, None)

# callable object with __call__ method
class Callable:
    def __call__(self, x):
        return x

Callable()(1)

# function
def func(x):
    return x

func(1)

# class
class Class:
    def __call__(self, x):
        return x

Class()(1)

# method
class Class:
    def method(self, x):
        return x

Class().method(1)

# built-in function
abs(-1)

# built-in method
[].append(1)

# generator function
def gen_func():
    yield 1

gen_func()

# generator
def gen_func():
    yield 1

gen = gen_func()
gen

# async generator function
import types

async def async_gen_func():
    yield 1

types.AsyncGeneratorType(async_gen_func(), {})

# async generator
import types


