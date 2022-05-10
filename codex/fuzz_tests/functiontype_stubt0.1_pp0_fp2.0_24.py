from types import FunctionType
a = (x for x in [1])
b = [1]
print(type(a))
print(type(b))
print(type(print))
print(type(FunctionType))
print(type(lambda x: x))
print(type(abs))
print(type(a) == type(b))
print(type(a) == type(print))
print(type(a) == type(FunctionType))
print(type(a) == type(lambda x: x))
print(type(a) == type(abs))

# 判断对象是否是函数
print(isinstance(print, FunctionType))
print(isinstance(lambda x: x, FunctionType))
print(isinstance(abs, FunctionType))
print(isinstance(a, FunctionType))

# 判断对象是否是可调用对象
print(callable(print))
print(callable(lambda x: x))
print(callable(abs))
print(callable(a))

# 判
