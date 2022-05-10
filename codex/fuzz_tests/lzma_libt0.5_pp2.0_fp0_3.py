import lzma
lzma.LZMAFile(fileobj=open('/tmp/foo.xz'))

# xz-utils
import subprocess
subprocess.check_call(['xz', '-d', '/tmp/foo.xz'])

# zlib
import zlib
zlib.decompress(open('/tmp/foo.zlib').read())

# zstd
import zstd
zstd.ZstdDecompressor().decompress(open('/tmp/foo.zst').read())
```

### Encoding

```python
# bz2
import bz2
bz2.compress(open('/tmp/foo').read())

# gzip
import gzip
gzip.compress(open('/tmp/foo').read())

# lzma
import lzma
lzma.LZMADictCompressor().compress(open('/tmp/foo').read())

# zlib
import zlib
zlib.compress(open('/tmp/foo').read())

# zstd
import z
