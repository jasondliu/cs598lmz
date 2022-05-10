from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
c = (x for x in [1])
d = (x for x in [1])
print(a == b == c == d)

# 生成器表达式，在python中，也是一个对象。生成器表达式在每次需要一个元素的时候，会计算出下一个元素。
# 生成器表达式可以用在需要迭代器的任何地方。
# 例如，如果你需要一个排序好的列表，但是不想构建完整的列表
