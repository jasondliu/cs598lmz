from types import FunctionType
list(FunctionType(lambda x: x).__code__.co_names)

import dis
dis.dis(lambda x: x)
def func(x):
    return x + 1

func.__code__.co_names
dis.dis(func)
func.__code__.co_code
func.__code__.co_code
import types
types.FunctionType(func.__code__, globals(), 'func2')
types.FunctionType(func.__code__, globals(), 'func2')()
import functools
functools.wrap_function(func, globals())
def func2(x):
    return x + 1
func2()
import functools
@functools.lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

[fib(n) for n in range(16)]
fib.cache_info()

import functools

@functools.lru_cache()
def fib(n
