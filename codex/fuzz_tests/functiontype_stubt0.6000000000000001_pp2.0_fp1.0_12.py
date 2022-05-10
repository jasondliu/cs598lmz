from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
# 判断是否是某个类的实例，类似于Java的instance of

# 判断是否是某个类的实例，类似于Java的instance of
print(isinstance(a, list))

# 判断是否是某个类的实例，类似于Java的instance of
print(isinstance(a, Iterator))

# 判断是否是某个类的实例，类似于Java的instance of
print(isinstance(a, Iterable))
