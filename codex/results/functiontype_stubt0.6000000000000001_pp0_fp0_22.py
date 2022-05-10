from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))

def func1():
    print("func1")

a = func1
print(a)
print(type(a))

b = [func1]
print(b)
print(type(b))

c = {func1:1}
print(c)
print(type(c))


# 判断一个对象是否是一个函数
print(isinstance(func1, FunctionType))
print(isinstance(print, FunctionType))
print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))
print(isinstance(c, FunctionType))

print(isinstance(a, list))
print(isinstance(b, list))
print(isinstance(c, dict))

# 判断一个对象是否可调用
from collections import Iterable, Iterator
print(callable(func1))
print(callable(print))
print(call
