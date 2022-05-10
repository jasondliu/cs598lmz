from types import FunctionType
a = (x for x in [1])
print(type(a))
# <class 'generator'>
print(a.__next__())
# 1
print(a.__next__())
# StopIteration

# 列表生成式
print([x for x in range(10)])
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print([x * x for x in range(10)])
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print([x * x for x in range(10) if x % 2 == 0])
# [0, 4, 16, 36, 64]
print([m + n for m in 'ABC' for n in 'XYZ'])
# ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

# 字典生成式
print({x: x * x for x in range(10)})
# {0: 0, 1: 1, 2:
