from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))


# 使用列表生成式生成一个列表，如果只想知道是否存在某个数
# 而不想生成一个数组，可以使用any()函数
# any([1, 2, 3, 4])
# any(['a', 'b', 'c', 'd'])

# 求1-100之间的所有数的平方和
# r = []
# for x in range(1, 101):
#     r.append(x * x)
# sum(r)

# 1-100之间的所有偶数的平方
# r = []
# for x in range(1, 101):
#     if x % 2 == 0:
#         r.append(x * x)
# sum(
