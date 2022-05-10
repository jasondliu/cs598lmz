from lzma import LZMADecompressor
LZMADecompressor().decompress(data)
```

## 压缩

```python
from lzma import LZMACompressor
compressor = LZMACompressor()
compressor.compress(b"some data")
compressor.flush()
```

## 压缩文件

```python
import lzma
with lzma.open("foo.xz", "w") as f:
    f.write(b"some data")
```

## 解压缩文件

```python
import lzma
with lzma.open("foo.xz") as f:
    file_content = f.read()
```

## 压缩文件夹

```python
import lzma
with lzma.open("foo.xz", "w") as f:
    f.write(b"some data")
```

## 解压缩文件夹

```python
import l
