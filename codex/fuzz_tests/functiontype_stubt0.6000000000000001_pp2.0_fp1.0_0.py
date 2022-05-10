from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type([]))
print(type(FunctionType))
print(dir(a))
print(dir([]))
print(dir(FunctionType))

# 可以通过callable函数判断是否可调用
print(callable(a))
print(callable([]))
print(callable(FunctionType))

# 除了可调用对象还有可迭代对象，可迭代对象iterable
# 可迭代对象都可以用for循环来遍历，可调用的对象不一定可迭代
# 所以可迭代的对象不一定可调用
# 可迭代对象的特
