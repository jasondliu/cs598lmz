from lzma import LZMADecompressor
LZMADecompressor().decompress(bytes).decode("utf-8")

# LZMA
```

```py
# via the gzip library
import gzip
gzip.decompress(bytes).decode("utf-8")

# gzip
```

```py
# via the zlib library
import zlib
zlib.decompress(bytes, zlib.MAX_WBITS|32).decode("utf-8")

# DEFLATE
```

```py
# via the bz2 library
import bz2
bz2.decompress(bytes).decode("utf-8")

# Bzip2
```

Or you could use the "zlib" library to decompress the whole thing.

```py
import zlib
zlib.decompress(bytes).decode("utf-8")

# ZIP
```

You could use the "lzma" library to decompress the whole thing.

```py
import lzma
lzma.decompress(bytes).decode
