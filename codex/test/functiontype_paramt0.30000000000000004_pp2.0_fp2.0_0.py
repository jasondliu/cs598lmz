from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__, closure=f.__closure__)
     for f in (lambda x: x + 1, lambda: 1))
# [<function __main__.<lambda>>, <function __main__.<lambda>>]

# 使用inspect模块的signature函数来获取函数的签名
from inspect import signature
