from types import FunctionType
list(FunctionType(lambda: 1).__closure__)

# FunctionType(lambda: 1).__code__.co_freevars

# 使用inspect模块的getclosurevars函数更好的获取函数的闭包变量
from inspect import getclosurevars
getclosurevars(FunctionType(lambda:1))

# 实现一个类似于Python2中的reduce
def reduce(func, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = func(value, element)
    return value

reduce(lambda x, y: x + y, [1, 2, 3, 4])

# 如果想使用迭代器计算累加器，可以
