from types import FunctionType
a = (x for x in [1])
print(a)

# 通过isinstance()函数判断一个对象是否是Iterable对象
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

# 使用enumerate()函数将list，tuple等可遍历对象转换成索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
