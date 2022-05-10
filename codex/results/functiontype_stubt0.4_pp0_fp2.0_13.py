from types import FunctionType
a = (x for x in [1])
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, Generator))
print(isinstance(a, FunctionType))

print('='*50)
# 生成器都是迭代器，但迭代器不一定是生成器
# 生成器是可迭代对象，但可迭代对象不一定是生成器

print('='*50)
# 可以使用isinstance()判断一个对象是否是Iterable对象
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

print('='*50)
# 可
