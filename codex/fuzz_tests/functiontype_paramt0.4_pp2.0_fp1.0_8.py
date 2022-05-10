from types import FunctionType
list(FunctionType(lambda:0,{}).__code__.co_varnames)

#%%
# 实现一个简单的装饰器
def log(func):
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('2018-04-03')

now()

#%%
# 实现一个装饰器，接受参数
def log(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s():' % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2018-04-03')

now()

#%%
# 实现一个装饰
