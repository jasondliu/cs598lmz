from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))

# 可迭代对象
# 可迭代对象，只要实现了__iter__方法，就是可迭代对象
# 可迭代对象，只要实现了__getitem__方法，并且抛出IndexError异常，就是可迭代对象

# 迭代器
# 迭代器，只要实现了__iter__方法，并且实现了__next__方法，就是迭代器
#
