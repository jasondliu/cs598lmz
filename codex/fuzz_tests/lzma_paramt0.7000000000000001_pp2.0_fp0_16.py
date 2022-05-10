from lzma import LZMADecompressor
LZMADecompressor.decompress(b'\xfd7zXZ\x00\x04\xe6\xd6B\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00')
#b'Hello World'
```

```py
from lzma import LZMAFile
with LZMAFile('example.xz') as f:
    data = f.read()
```
## 数据压缩与解压

### 压缩

- zlib
- gzip
- bz2
- lzma

### 解压

- zlib
- gzip
- bz2
- lzma
- zipfile
- tarfile

```py
import zlib
s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
len(t)

zlib.decompress(t)

zlib
