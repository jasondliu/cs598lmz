from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a)
print(b)
print(a == b)
print(id(a))
print(id(b))
print(a is b)
print(type(a))
print(type(b))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))


# 列表生成式
# 生成[1x1, 2x2, 3x3, ..., 10x10]
L = [x * x for x in range(1, 11)]
print(L)

# 生成全排列
L = [m + n for m in 'ABC' for n in 'XYZ']
print(L)

# 列出当前目录下的所有文件和目录名
import os
L = [d for d in os.listdir('.')]
print(L)


# 列表生成
