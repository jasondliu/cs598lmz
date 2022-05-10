fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
try:
    fn()
except TypeError as e:
    print(e)

# 使用装饰器实现单例模式
def singleton(cls):
    instances = {}
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getinstance

@singleton
class MyClass(object):
    a = 1

one = MyClass()
two = MyClass()
print(id(one), id(two))

# 使用装饰器实现缓存
import functools

def cache(func):
    cache = {}
    @functools.wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

@cache
def fib(n):

