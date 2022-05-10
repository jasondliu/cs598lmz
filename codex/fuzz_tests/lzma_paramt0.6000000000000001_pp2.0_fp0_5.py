from lzma import LZMADecompressor
LZMADecompressor.decompress(b'x\x9cK\xcbH\xcd\xc9\xc9W(\xcf/\xcaI\x01\x00\x04\xe6\xd6\xb4J')
b'Hello World'

>>>
```

## Reference

### class lzma.LZMADecompressor

```
class lzma.LZMADecompressor(format=FORMAT_AUTO, check=-1, preset=None, filters=None)
```

| class |
| :-- |
| LZMADecompressor |

| parameters |
| :-- |
| format | 
| check | 
| preset | 
| filters | 

| methods |
| :-- |
| decompress(data) |
| flush() |

## Examples

### Example: Decompress a memoryview

```
>>> import lzma
>>> import binascii
>>> data = '5d0000800000ffffffff0c48656c6c6f2c20
