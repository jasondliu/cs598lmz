import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

import functools
def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('decorator')
        return func(*args, **kwargs)
    return wrapper

@decorator
def myfunc():
    print('myfunc')

myfunc()

print('myfunc:', myfunc)

def myfunc2(s):
    print('myfunc2:', s)

f = myfunc2

print('f:', f)

functype = type(f)
print('functype:', functype)

def myfunc3(s):
    print(s)

myfunc3('myfunc3')

myfunc3.__call__('myfunc3')

print('myfunc3:', myfunc3)
print('callable:', callable(myfunc3))

print('myfunc3.__call__:', myfunc3.__call__)
print('
