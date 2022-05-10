from lzma import LZMADecompressor
LZMADecompressor()
from lzma import open as lzopen
lzopen('file.lzma')
```

```
$ python3
Python 3.7.0 (default, Aug  9 2018, 17:23:01) 
[Clang 9.0.0 (clang-900.0.39.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import lzma
>>> lzma.LZMADecompressor()
<lzma.LZMADecompressor object at 0x10a5b8668>
>>> 
```

### 4. Compress data in memory with LZMA

```
from lzma import compress, decompress
compressed = compress(b'a' * 1048576) # b'a' * 1024 * 1024
len(compressed)
decompressed = decompress(compressed)
len(decompressed)
decompressed == b'a' * 1048576
```

```
$ python3
Python 3.
