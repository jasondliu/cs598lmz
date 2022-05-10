from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, FunctionType))

print(isinstance(a, GeneratorType))

# 判断是否是某种类型的实例
print(isinstance(a, (GeneratorType, FunctionType)))

# 判断是否是某种类型的子类
print(issubclass(GeneratorType, FunctionType))
