from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.BZ2File("compressed.bz2").read())
```

```
import zlib
zlib.decompress(open("compressed.zlib").read())
```

```
gzip.open("compressed.gz").read()
```

```
import lzma
lzma.LZMADecompressor().decompress(open("compressed.xz").read())
```

```
import lz4
lz4.block.decompress(open("compressed.lz4").read())
```

```
import brotli
brotli.decompress(open("compressed.br").read())
```

```
import lzma
lzma.LZMADecompressor().decompress(open("compressed.xz").read())
```

```
import zstandard
zstandard.ZstdDecompressor().decompress(open("compressed.zst").read())
```


# Comp
