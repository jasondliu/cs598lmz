import bz2
bz2.BZ2File(filename)

import gzip
gzip.open(filename, mode='rt')

import lzma
lzma.LZMAFile(filename)

import zipfile
zf = zipfile.ZipFile(filename)
zf.open(zf.namelist()[0])
```

## Example

```python
import sys
import gzip
import bz2
import lzma
import zipfile

import magic

filename = sys.argv[1]

mime = magic.from_file(filename, mime=True)

if mime == 'application/x-gzip':
    fh = gzip.open(filename, mode='rt')
elif mime == 'application/x-bzip2':
    fh = bz2.BZ2File(filename)
elif mime == 'application/x-xz':
    fh = lzma.LZMAFile(filename)
elif mime == 'application/zip':
    zf = zipfile.ZipFile(filename
