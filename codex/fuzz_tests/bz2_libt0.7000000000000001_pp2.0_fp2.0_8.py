import bz2
bz2.BZ2File(filename)

# or, with context manager
with bz2.BZ2File(filename) as fileobj:
    content = fileobj.read()

# or, with gzip
import gzip
gzip.open(filename)

# or, with context manager
with gzip.open(filename) as fileobj:
    content = fileobj.read()

# or, with lzma
import lzma
lzma.open(filename)

# or, with context manager
with lzma.open(filename) as fileobj:
    content = fileobj.read()
 
# or, with context manager
with open(filename, 'rb') as fileobj:
    content = xz.decompress(fileobj.read())
```

## 解析JSON文件

```python
import json
with open('data.json') as f:
    data = json.load(f)
```

## 读取二进制数据到
