from types import FunctionType
list(FunctionType(f.__code__, {}, "foo"))

# 使用lambda 是一种简便的定义小函数的方法
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0)
f(1)

# lambda 可以用在任何需要函数的地方
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
pairs

# documentation strings
def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)

# 函数也是对象，有自己的属性和方法

