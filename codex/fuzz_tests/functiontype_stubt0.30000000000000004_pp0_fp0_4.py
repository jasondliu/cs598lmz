from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__iter__))
print(type(a.__iter__) == FunctionType)
print(type(a.__iter__) == types.FunctionType)

# 判断一个对象是否是函数
print(callable(a))
print(callable(a.__next__))
print(callable(a.__iter__))

# 判断一个对象是否是类
print(isinstance(a, type))
print(isinstance(a, types.GeneratorType))
print(isinstance(a, types.FunctionType))

# 判断一个对象是否是模块
print(isinstance(types, types.ModuleType))
print(isinstance(types, types.FunctionType))

# 判断一个对象是否是类型
