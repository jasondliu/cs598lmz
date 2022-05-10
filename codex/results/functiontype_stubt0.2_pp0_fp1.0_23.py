from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__iter__))
print(type(a.__next__))
print(type(a.__next__) == FunctionType)
print(a.__next__())
print(a.__next__())

# 可迭代对象
# 可以被for循环的对象
# 可以被next()函数调用的对象
# 可以被iter()函数调用的对象
# 可以被list()函数调用的对象
# 可以被tuple()函数调用的对象
# 可以被set()函数调用的对象
# 可以被dict()函数调用
