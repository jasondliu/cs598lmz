from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))

# 判断是否是某种类型
print(isinstance(a, Iterator))

# 判断是否是某种类型
print(isinstance(a, Iterable))

# 判断是否是某种类型
print(isinstance(a, FunctionType))

# 判断是否是某种类型
print(isinstance(a, GeneratorType))

# 判断是否是某种类型
print(isinstance(a, list))

# 判断是否是某种类型
print(isinstance(a, tuple))

# 判断是否是某种类型
print(isinstance
