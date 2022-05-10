from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(lambda x: x))
print(type(FunctionType))
print(type(FunctionType(lambda x: x, globals())))

# 判断是不是某个类型
print(isinstance(a, GeneratorType))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, (Iterator, Iterable)))

# 判断是不是某个类型
print(issubclass(GeneratorType, Iterator))
print(issubclass(GeneratorType, Iterable))
print(issubclass(GeneratorType, (Iterator, Iterable)))

# 判断是不是某个类型
print(isinstance(a, FunctionType))
print(issubclass(GeneratorType, FunctionType))

# 判断是不是某个类型
print(isinstance(a,
