from types import FunctionType
list(FunctionType(f.__code__,globals()).__globals__.keys())

# 2. 实现一个“速度”装饰器，可以计算一个函数执行的时间
def speed(a):
    def wapper(b):
        def run(*args, **kwargs):
            print('啊啊啊')
            a(b, *args, **kwargs)
        return run
    return wapper

@speed
def f1(*args, **kwargs):
    print('执行f()...')

# f1('a','b','c')

# 3. 实现一个验证用户权限的装饰器
def validate_user_permission(func):
    def wrapper(*args, **kwargs):
        if session.get('username') is not None:
            func(*args, **
