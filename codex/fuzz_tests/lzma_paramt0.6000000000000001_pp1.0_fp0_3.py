from lzma import LZMADecompressor
LZMADecompressor.decompress(b'...')
```

如果要支持续传，使用 lzma.open() 函数代替 lzma.LZMADecompressor 类：

```python
from lzma import open
with open('example.xz', 'rb') as f:
    file_content = f.read()
```

## 写入压缩文件

使用 io.BytesIO() 将压缩数据写入内存中：

```python
import io
import lzma

with lzma.open('file.xz', 'w') as f:
    f.write(b'Hello World')

buf = io.BytesIO()
with lzma.open(buf, 'w') as f:
    f.write(b'Hello World')

print(buf.getvalue())
```


