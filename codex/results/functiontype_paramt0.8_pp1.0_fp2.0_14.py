from types import FunctionType
list(FunctionType(code, globals=globals(), name="func").__closure__)

# 匿名函数
def add(x, y, f):
    return f(x) + f(y)
add(-1, -2, lambda x: x * x)

# 装饰器
def log(func):
    def wrapper(*args, **kw):
        print("call %s():" % (func.__name__))
        return func(*args, **kw)
    return wrapper
@log
def now():
    print("2014-02-01")
now()

# 偏函数
int("123")
int("12345", base=8)
int("12345", base=16)
int2 = functools.partial(int, base=2)
int2("1000000")
