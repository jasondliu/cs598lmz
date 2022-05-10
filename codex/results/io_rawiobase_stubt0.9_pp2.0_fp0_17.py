import io
class File(io.RawIOBase):

def __init__(self, file):
    self.file = open(file, 'rb')

def readinto(self, b):
    return self.file.readinto(b)
```

```python
from io import FileIO
f = FileIO('file.txt', mode='w', closefd=True)
f.fileno()
```
-----------------------------------------------------------------------------------------------------
#### 修改你的代码以使用 io.StringIO 和 io.BytesIO
##### io.StringIO 模块
BytesIO 是一个在内存中操作二进制数据的类. 它提供一种类文件对象的接口, 可用于在内存中读写不是真实存在的文件.
此模块提供基
