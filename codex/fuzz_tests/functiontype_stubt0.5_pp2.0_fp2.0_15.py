from types import FunctionType
a = (x for x in [1])
print(a)
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, list))

# 判断一个类是否是另一个类的子类
print(issubclass(list, object))
print(issubclass(list, GeneratorType))
print(issubclass(GeneratorType, object))
print(issubclass(GeneratorType, list))

# 判断一个对象是否是另一个类的实例
print(isinstance(a, GeneratorType))
print(isinstance(a, list))
print(isinstance(a, object))
print(isinstance(a, FunctionType))

# 判断一个对象是否是另一个类的子类
print(issubclass(GeneratorType, object))
print(issubclass(GeneratorType, list))
print(
