from types import FunctionType
list(FunctionType(add, globals())(1,2))

# 但是，反过来，先定义函数，再获得函数的code对象，
# 比方说准备把一个函数通过网络让别的机器执行，这种场景比较适合。

def add(x, y):
    return x + y

import types
code = add.__code__
new_func = types.FunctionType(code, globals(), name='add', argdefs=(), closure=())
add(1, 2)
new_func(1, 2)

# 通过types模块定义的常量，来判断一个变量的类型，
