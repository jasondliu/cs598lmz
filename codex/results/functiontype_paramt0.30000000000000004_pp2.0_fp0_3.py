from types import FunctionType
list(FunctionType(lambda: None).__code__.co_varnames)

# ['x', 'y']

# 使用函数的 __code__ 属性的 co_varnames 属性，可以获取函数的参数名称，但是它只能获取到最外层函数的参数名称。
# 如果要获取内层函数的参数名称，可以使用 inspect 模块的 signature 函数。

from inspect import signature

sig = signature(lambda x, y: None)
sig.parameters['x'].name

# 'x'

# 如果要获取函数的返回值，可以使用
