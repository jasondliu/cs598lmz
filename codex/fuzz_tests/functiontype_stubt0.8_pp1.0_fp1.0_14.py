from types import FunctionType
a = (x for x in [1])
print(type(a))

b = lambda x: x*2
print(isinstance(b,FunctionType)) # true

# 装饰器：在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
# 函数对象有一个__name__属性，可以拿到函数的名字：



def log(func):
    def wrapper(*args,**kw):
        print('call %s():'%func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('2018-1-20')

now()

# 偏函数
# int2 = functools.partial(int,base=2)
# int2
