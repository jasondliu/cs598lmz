from types import FunctionType
a = (x for x in [1])
b = lambda x : 1
print(isinstance(a,FunctionType)) #True
print(isinstance(b,FunctionType)) #True

# 另一方面, 匿名函数可以继承自FunctionType类型
import functools
FunctionType.__subclasshook__ = lambda C, S : True
isinstance(a,FunctionType) # True
isinstance(b,FunctionType) # True

# 闭包(closures)
# Python是一门能够扩展的语言, 通过编码技术可以在运行时修改代码.
# 在一个方法中添加新的解释器操作符, 定义新的内置函数, 修改现有
