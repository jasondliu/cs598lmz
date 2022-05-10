import lzma
lzma.LZMADecompressor().decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00')
# b'foobar'
```

```python
import lzma
lzma.LZMADecompressor().flush(b'foobar')
# b'foobar'
```

```python
import lzma
lzma.LZMADecompressor().decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00')
# b'foobar'
```


**三种解压方法**

1. 直
