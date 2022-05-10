from types import FunctionType
a = (x for x in [1])
b = [x for x in 'abc']
# a对象是一个生成器，本身不是一个列表
print(type(a), FunctionType)
print(type(FunctionType))

import inspect
print(inspect.isgeneratorfunction(a))
