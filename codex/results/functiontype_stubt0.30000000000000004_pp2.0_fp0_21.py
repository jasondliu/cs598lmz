from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(lambda x: x))
print(type(FunctionType))

# 判断对象是否是函数
from types import FunctionType
print(isinstance(lambda x: x, FunctionType))
print(isinstance(lambda x: x, (FunctionType, int)))

# 判断对象是否是某种类型
from types import FunctionType
print(isinstance(lambda x: x, FunctionType))
print(isinstance(lambda x: x, (FunctionType, int)))

# 查看对象的所有属性
from types import FunctionType
print(dir(FunctionType))

# 查看对象的所有属性
from types import FunctionType
print(dir(FunctionType))

# 查看对象的所有属性
from types import FunctionType
print(
