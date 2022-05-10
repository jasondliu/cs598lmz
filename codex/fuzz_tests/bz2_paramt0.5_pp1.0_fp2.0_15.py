from bz2 import BZ2Decompressor
BZ2Decompressor().decompress()

from gzip import GzipFile
GzipFile().read()

from zlib import decompress
decompress()
```

```
import zlib
zlib.decompress()

import zipfile
zipfile.ZipFile().read()
zipfile.ZipFile().extractall()

import tarfile
tarfile.TarFile().extractall()
```
