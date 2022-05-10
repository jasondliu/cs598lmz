import types
types.FunctionType

# 判断是否是迭代器
from collections import Iterable
isinstance([],Iterable)

# 判断是否是可迭代对象
from collections import Iterator
isinstance((x for x in range(10)),Iterator)

# 列表生成式
[x * x for x in range(1, 11)]
[x * x for x in range(1, 11) if x % 2 == 0]
[m + n for m in 'ABC' for n in 'XYZ']
# 列出当前目录下的所有文件和目录名
import os
[d for d in os.listdir('.')]
d = {'x': 'A', 'y': 'B', 'z': 'C' }
[k + '=' + v for k, v in d.items()]
L = ['Hello', 'World', 'IBM', 'Apple']
