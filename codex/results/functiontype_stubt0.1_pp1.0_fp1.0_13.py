from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__iter__))
print(type(a.__next__) == type(a.__iter__))
print(type(a.__next__) == FunctionType)
print(type(a.__iter__) == FunctionType)
print(type(a.__next__) == type(a.__iter__) == FunctionType)

# 可迭代对象
# 可迭代对象：可以使用for循环的对象
# 可迭代对象：可以使用in判断的对象
# 可迭代对象：可以使用list()函数转换的对象
# 可迭代对象：可以使用tuple()函
