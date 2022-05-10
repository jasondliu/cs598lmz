from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__,
                  closure=f.__closure__) for f in (lambda x: x, lambda x, y: x + y))
# [<function <lambda> at 0x7f5e6c8c8d90>, <function <lambda> at 0x7f5e6c8c8e18>]

# 使用inspect.getcallargs()函数，可以检查函数的参数是否正确，并返回一个参数字典。
import inspect
def f(a, b, c=1, *args, **kwargs):
    pass
inspect.getcallargs(f, 1, 2, 3, 4, 5, 6, foo=1, bar=2)
# {'a': 1, 'b': 2, 'c': 3, 'args': (4, 5
