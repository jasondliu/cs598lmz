from types import FunctionType
a = (x for x in [1])
print(type(a))
# 判断是否是迭代器
print(isinstance(a, Iterator))
# 是否是可迭代对象
print(isinstance(a, Iterable))
# 是否是生成器
print(isinstance(a, Generator))
# 是否是函数
print(isinstance(abs, FunctionType))
# 是否是元祖
print(isinstance((1, 2), Tuple))


# 可以用enumerate函数把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
#
