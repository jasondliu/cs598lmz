from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))


# 函数式编程

# 高阶函数：可接受函数作为参数并返回函数作为结果的函数
def add(x, y, f):
    return f(x) + f(y)


print(add(3, -7, abs))

# map
def fun1(x):
    return x * x


print(list(map(fun1, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# reduce
from functools import reduce
def fun2(x, y):
    return x * 10 + y
print(reduce(fun2, [1, 3, 5, 7, 9]))

# 转换
