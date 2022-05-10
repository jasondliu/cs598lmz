from types import FunctionType
a = (x for x in [1])
b = lambda x:x
c = list
assert isinstance(a, GeneratorType)
assert isinstance(b, FunctionType)
assert isinstance(c, type)
```

```py
# 列表生成式
L = [x * x for x in range(10)]
print(L)

# 使用两层循环，可以生成全排列：
L = [m + n for m in 'ABC' for n in 'XYZ']
print(L)

# 列出当前目录下的所有文件和目录名，可以通过一行代码实现：
import os
L = [d for d in os.listdir('.')]
print(L)

# 生成器
# 如果列表元素
