import lzma
lzma.decompress(data)

# 打开压缩文件
with lzma.open('file.xz', 'rt') as f:
    text = f.read()

# 写入压缩文件
with lzma.open('file.xz', 'wt') as f:
    f.write(text)

# 压缩文件对象支持上下文管理协议，可以自动关闭
with lzma.open('file.xz', 'rt') as f:
    text = f.read()

# 压缩文件对象支持迭代
with lzma.open('file.xz', 'rt') as f:
    for line in f:
        print(line)
```

### bz2

```python
import bz2

