from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(print))
print(type(lambda x: x))
print(type(FunctionType))

# 判断对象是否是函数
print(callable(a))
print(callable(print))
print(callable(lambda x: x))
print(callable(FunctionType))

# 判断对象是否是某个类型
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, Generator))
print(isinstance(a, FunctionType))
print(isinstance(print, FunctionType))
print(isinstance(lambda x: x, FunctionType))
print(isinstance(FunctionType, FunctionType))

# 判断对象是否是某个类型的子类
print(issubclass(Iterator, Iterable))
print(issubclass(Iterator, Generator))
print
