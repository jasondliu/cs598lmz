from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(type(a) is GeneratorType)

b = FunctionType(lambda x: x, {})
print(type(b))
print(isinstance(b, FunctionType))
print(type(b) is FunctionType)

# 判断是否是可调用对象
print(callable(a))
print(callable(b))

# 判断是否是类
print(isinstance(b, type))
print(type(b) is type)

# 判断是否是类实例
print(isinstance(b, object))
print(type(b) is object)

# 判断是否是类型
print(isinstance(b, type))
print(type(b) is type)

# 判断是否是类型实例
print(isinstance(b
