from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(print))
print(type(FunctionType))

# 判断对象是否是函数
print(callable(a))
print(callable(print))
print(callable(FunctionType))

# 判断对象是否是可迭代对象
print(isinstance(a, Iterable))
print(isinstance(print, Iterable))
print(isinstance(FunctionType, Iterable))

# 判断对象是否是迭代器
print(isinstance(a, Iterator))
print(isinstance(print, Iterator))
print(isinstance(FunctionType, Iterator))

# 判断对象是否是生成器
print(isinstance(a, Generator))
print(isinstance(print, Generator))
print(isinstance(FunctionType, Generator))

# 判断对象是
