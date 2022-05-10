from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_compressed)

# or

import bz2
bz2.decompress(bz2_compressed)
```

## gzip

```python
# compress
import gzip
with gzip.open('out.gz', 'wb') as fout:
    fout.write(b'hello world')

# decompress
import gzip
with gzip.open('out.gz', 'rb') as fin:
    print(fin.read())
```
