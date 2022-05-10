from lzma import LZMADecompressor
LZMADecompressor().decompress(data)
 
# b'Hello World!'
```

##### xz

```python
import lzma
with lzma.open('hello.xz', 'rt') as f:
    print(f.read())
```

```python
import lzma
with lzma.open('hello.xz', 'wt') as f:
    f.write('Hello World!')
```

```python
import lzma
with lzma.open('hello.xz', 'wt', preset=9) as f:
    f.write('Hello World!')
```

##### zlib

```python
import zlib
s = b'witch which has which witches wrist watch'
len(s)
# 41

t = zlib.compress(s)
len(t)
# 37

zlib.decompress(t)
# b'witch which has which witches wrist watch'

zlib.crc32(s)
# 226805979
```

#####
