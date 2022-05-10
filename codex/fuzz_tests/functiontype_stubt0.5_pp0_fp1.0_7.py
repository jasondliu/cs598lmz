from types import FunctionType
a = (x for x in [1])
b = (x for x in [2])
a.__next__()

a = [1, 2, 3]
b = [4, 5, 6]
for x, y in zip(a, b):
    print(x, y)

# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
# 我们可以使用 list() 转换来输出列表。
# 如果各个迭代器的元素个
