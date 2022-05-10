from lzma import LZMADecompressor
LZMADecompressor().decompress(b"\x5d\x00\x00\x80\x00")

<class 'lzma.LZMADecompressor'>

from lzma import LZMADecompressor
LZMADecompressor().decompress(b"\xfd\x37\x7a\x58\x5a\x00")

<class 'lzma.LZMADecompressor'>

from lzma import LZMADecompressor
LZMADecompressor().decompress(b"\x59\x5a\x20\x00\x00\x00")

<class 'lzma.LZMADecompressor'>

from lzma import LZMADecompressor
LZMADecompressor().decompress(b"\xfd\x37\x7a\x58\x5a\x00")

<class 'lzma.LZMADecompressor'>
```

```
echo -e "\x5d
