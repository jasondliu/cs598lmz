from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

# 判断是否是某个类型
print(isinstance([1, 2, 3], (list, tuple)))

# 判断是否是某个类型
print(isinstance((1, 2, 3), (list, tuple)))

# 判断是否是某个类型
print(isinstance(123, (list, tuple)))

# 判断是否是某个类型
print(isinstance('abc', (list, tuple)))

# 判断是否是某个类型
print(isinstance(b'abc', (list, tuple)))

# 判断是否是某个类型
print(isinstance(abs, (list, tuple)))

# 判
