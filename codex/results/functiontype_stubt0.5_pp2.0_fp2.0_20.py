from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(type(a) is GeneratorType)
print(type(a) is FunctionType)

# 判断是否是某个类型
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, Iterator))

# 判断是否是某个类型的子类
print(issubclass(GeneratorType, GeneratorType))
print(issubclass(GeneratorType, FunctionType))
print(issubclass(GeneratorType, Iterator))

# 判断是否是某个类型的子类
print(issubclass(Iterator, Iterator))
print(issubclass(Iterator, FunctionType))
print(issubclass(Iterator, GeneratorType))

# 判断是否是某个类型的子
