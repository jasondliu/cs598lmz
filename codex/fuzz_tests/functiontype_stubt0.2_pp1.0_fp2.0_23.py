from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

# 判断一个对象是否是可调用对象
print(callable(a))

# 判断一个对象是否是某个类型的实例
print(isinstance(a, GeneratorType))

# 判断一个对象是否是某个类型的子类
print(issubclass(GeneratorType, FunctionType))

# 判断一个对象是否是某个类型的子类
print(issubclass(GeneratorType, FunctionType))

# 判断一个对象是否是某个类型的子类
print
