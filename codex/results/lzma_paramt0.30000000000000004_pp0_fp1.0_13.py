from lzma import LZMADecompressor
LZMADecompressor().decompress(open('data/data.xz', 'rb').read())

# bz2
from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open('data/data.bz2', 'rb').read())

# zlib
import zlib
zlib.decompress(open('data/data.zlib', 'rb').read())

# gzip
import gzip
gzip.decompress(open('data/data.gz', 'rb').read())

# tar
import tarfile
tar = tarfile.open('data/data.tar')
tar.extractall()
tar.close()

# zip
import zipfile
zip = zipfile.ZipFile('data/data.zip')
zip.extractall()
zip.close()
```

## 字符串

### 字符串分割

```python
# 字符串分割
'a,b,c'.split(',')


