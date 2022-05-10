from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(sum))
print(type(FunctionType))

"""

# 元组
"""
t1 = (1, 1.2, 'hello')
t2 = (1,)  # 只有一个元素的元组，需要加逗号
print(t1[2])
print(t2)
t3 = t1 + (2,) + t2 + ((1, 2), (3, 4))
print(t3)

for i in t3:
    print(i, end=' ')
print()

t4 = 1, 2, 3, 4
t5 = 1, 'hello', (1, 2, 3)
print(t4)
print(t5)
# print(min(t4))

a = 20
b = 30
a, b = b, a
print(a, b)

nums = [1, 2, 3, 4]
a, b, c, d = nums
