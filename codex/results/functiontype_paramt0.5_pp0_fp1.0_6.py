from types import FunctionType
list(FunctionType(f.__code__, globals(), 'f') for f in (lambda: x, lambda: y))
# [<function <lambda> at 0x7f8f8d9c7e18>, <function <lambda> at 0x7f8f8d9c7ea0>]

# 上面的代码是一个技巧，可以用它来编写一个函数，它能返回函数的名称：
def get_name(f):
    return f.__name__
get_name(lambda x: x)
# '<lambda>'

# 如果一个函数的第一个参数是callable的，那么它就可以当做装饰器来使用。比如，下面的代码
