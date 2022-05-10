from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, IteratorType))
print(isinstance(a, IterableType))
print(isinstance(a, FunctionType))

print(isinstance(iter(a), IteratorType))
print(isinstance(iter(a), IterableType))
print(isinstance(iter(a), FunctionType))

print(isinstance(iter(a), GeneratorType))


# 可迭代对象, 迭代器, 生成器的区别
# 可迭代对象: 只要实现__iter__方法, 就是可迭代对象, 可迭代对象只能用__next__方法获取下一个元素
# 迭代器: 可迭代对象的__iter__方法返回的
