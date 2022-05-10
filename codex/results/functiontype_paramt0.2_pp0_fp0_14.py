from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# 函数的属性
def f():
    pass

f.__name__
f.__doc__
f.__defaults__
f.__code__
f.__globals__
f.__dict__

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
import functools
int2 = functools.partial(int, base=2)
int2('1000000')

# 模块
# 导入模块
import sys
sys.path

# 模块搜索路径
# 当我们试
