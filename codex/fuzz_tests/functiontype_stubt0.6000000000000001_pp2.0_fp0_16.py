from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(FunctionType))

# 列表生成式
print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])
# 列出当前目录下的所有文件和目录名，可以通过一行代码实现
print([d for d in os.listdir('.')])
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, '=', v)
print([k + '=' + v for k, v in d.items()])
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

#
