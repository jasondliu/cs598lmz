from lzma import LZMADecompressor
LZMADecompressor().decompress(data)
```

```
#!python

from zlib import decompress
decompress(data)
```

```
#!python

from gzip import decompress
decompress(data)
```

```
#!python

from bz2 import decompress
decompress(data)
```

```
#!python

import snappy
snappy.uncompress(data)
```

```
#!python

import bz2
bz2.decompress(data)
```

##### The 3rd Party Package: backports.lzma

https://pypi.python.org/pypi/backports.lzma

The backports.lzma module provides a simple interface for decompressing LZMA-compressed data and files. It is compatible with the Python standard library’s lzma module.

```
#!python

import lzma
lzma.LZMADecompressor().decompress(data
