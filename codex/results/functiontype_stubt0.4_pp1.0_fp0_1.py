from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(lambda x: x))
print(type(FunctionType))
print(type(abs))
print(type(a) == type([]))
print(type(a) == type(lambda x: x))
print(type(a) == type(FunctionType))
print(type(a) == type(abs))
# 判断一个对象是否是函数
print(isinstance(a, FunctionType))
print(isinstance(lambda x: x, FunctionType))
print(isinstance(abs, FunctionType))
print(isinstance(a, Iterator))
print(isinstance([], Iterator))
print(isinstance(iter([]), Iterator))
# 判断一个对象是否是可调用对象
print(callable(a))
print(callable(lambda x: x))
print(callable(abs))
print(callable(max))
print(callable([].append))
print(
