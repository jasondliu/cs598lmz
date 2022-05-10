from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# 函数的属性
def f():
    pass

print(f.__name__)
print(f.__doc__)
print(f.__code__)
print(f.__code__.co_varnames)
print(f.__code__.co_argcount)

# 函数的装饰器
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')

now()

# 偏函数
int('12345', base=8)

def int2(x, base=2):
    return int(x, base)

print(int2('1000000'))

import functools
int2 = functools.partial(int, base=2)
print(int2('1
