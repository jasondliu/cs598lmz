import ctypes
ctypes.cast(id(a), ctypes.py_object).value

#%%
def fib(n):
    print('fib({})'.format(n))
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

#%%
fib(5)

#%%
fib_cache = {}
def fib_cached(n):
    print('fib({})'.format(n))
    if n in fib_cache:
        return fib_cache[n]
    if n <= 1:
        return n
    else:
        fib_cache[n] = fib_cached(n - 1) + fib_cached(n - 2)
        return fib_cache[n]

#%%
fib_cached(5)

#%%
# import functools
# @functools.lru_cache(maxsize=None)
def fib_cached_v2(n):
    print('fib({})'.format(n))
    if n <= 1:
        return n
