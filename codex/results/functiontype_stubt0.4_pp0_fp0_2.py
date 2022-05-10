from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__next__) == FunctionType)
print(type(a.__iter__))
print(type(a.__iter__) == FunctionType)

# 函数的参数
def f(a, b, *args, c, d=1, **kwargs):
    print(a, b, args, c, d, kwargs)

f(1, 2, 3, 4, c=5, e=6)

# 函数的嵌套
def f(a):
    def g(b):
        return a + b
    return g

print(f(1)(2))

# 函数的闭包
def f(a):
    def g(b):
        return a + b
    return g

print(f(1)(2))

# 函数的装饰器
def deco(func):
    def wrapper(*args, **
