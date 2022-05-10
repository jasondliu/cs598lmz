from types import FunctionType
a = (x for x in [1])
print(isinstance(a, FunctionType))

def test(isinstance):
    print('test')

test(isinstance)

# 返回一个函数，并且在返回时把函数类型改为Test


def func():
    def test():
        print('this is test')
    return test


print(type(func()))


def test1(func):
    print('this is test1')
    return func


def test2(func):
    print('this is test2')
    return func


def test3():
    print('this is test3')

test3 = test1(test2(test3))
test3()

# 装饰器模式

import time


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


