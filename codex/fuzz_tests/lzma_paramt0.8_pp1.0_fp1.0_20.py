from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x1c\x00\x00\x00t/\xe5\xa3\x01\x00\x00\x04(B\xc5/\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
b''
>>>
```

This shows that the lzma module is not vulnerable.

References:

https://bugs.python.org/issue18308

https://github.com/python/cpython/commit/4f4b38ed7c25e504728e7f60ea3d0df69fe9c9b2
