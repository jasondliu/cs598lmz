from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)
```

### 循环控制

```python
# 在一个循环中同时迭代两个或多个序列
from itertools import zip_longest

names = ['Cecilia', 'Lise', 'Marie']
letters = [len(n) for n in names]

longest_name = None
max_letters = 0
for name, count in zip_longest(names, letters, fillvalue='?'):
    if count > max_letters:
        longest_name = name
        max_letters = count

print(longest_name)
# Marie
```

### 创建内存映射的二进制文件

```python
# 内存映射并不适用于大型文件（在内存中映射一个大文
