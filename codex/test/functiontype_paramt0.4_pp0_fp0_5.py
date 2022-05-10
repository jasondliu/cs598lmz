from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__, closure=f.__closure__)
     for f in (lambda x: x, lambda x, y=2: x + y))
# [<function <lambda> at 0x7f24d8e8cbf8>,
#  <function <lambda> at 0x7f24d8e8cae8>]

# The FunctionType constructor is not available in Python 2.
# In Python 2, you can use the following code to create a function object:
# def make_function(code, globs, name=None, argdefs=(), closure=None):
#     return FunctionType(code, globs, name, argdefs, closure)

# 创建一个函数对象，并将其赋值给一个变量

def f(x, y=2):
    return x + y

