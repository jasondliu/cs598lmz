from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)
## ['x']

#在函数中添加多个元素
def func(x, y, z):
    print(x, y, z)
func(1, 2, 3)
## 1 2 3

#获取函数参数列表
def func(x, y, z):
    print(x, y, z)
func.__code__.co_varnames
## ('x', 'y', 'z')

#闭包
def func(x):
    def inner():
        print(x)
    return inner
closure = func(1)
closure.__code__.co_freevars
## ('x',)

#装饰器
def decorator(func):
    def inner(*args, **kwargs):
        print('Start')
        func(*args, **kwargs)
        print('End')
    return inner

@decorator
