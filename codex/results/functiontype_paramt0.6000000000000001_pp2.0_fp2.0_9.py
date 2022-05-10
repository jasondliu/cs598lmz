from types import FunctionType
list(FunctionType(lambda x: x, {}).__code__.co_varnames)

#  判断是否为函数
from collections import Callable
callable(lambda x: x)

#  为函数添加属性
from functools import wraps
def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """wrapper docstring"""
        return func(*args, **kwargs)
    return wrapper
@decorator
def example():
    """example docstring"""
    print('Called example function')
example()
example.__name__
example.__doc__

#  为函数定义参数默认值
def foo(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)
foo(3, 7)
foo(25, c=24)
foo(c=50, a
