from types import FunctionType
a = (x for x in [1])
b = [1]
print(isinstance(a, GeneratorType))
print(isinstance(b, GeneratorType))
print(isinstance(a, Iterator))
print(isinstance(b, Iterator))
print(isinstance(a, Iterable))
print(isinstance(b, Iterable))
print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))

# 可迭代对象，可迭代对象是一个实现了__iter__方法的对象
# 迭代器，迭代器是一个实现了__iter__和__next__方法的对象
# 生成器，生成器是一个实现了__iter__和__next__方法的函数
# 可迭代对象，
