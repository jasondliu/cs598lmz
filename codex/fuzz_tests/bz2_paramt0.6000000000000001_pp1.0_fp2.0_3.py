from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bytes)
```

```python
import bz2
bz2.decompress(bytes)
```

```python
import zlib
zlib.decompress(bytes)
```

```python
import gzip
gzip.decompress(bytes)
```

```python
import lzma
lzma.decompress(bytes)
```

```python
import lzma
lzma.decompress(bytes, format=lzma.FORMAT_RAW)
```

```python
import zlib
zlib.decompress(bytes, wbits=-15)
```

```python
import zlib
zlib.decompress(bytes, wbits=15 | 32)
```

### Encode

```python
import binascii
binascii.b2a_base64(bytes)
```

```python
import base64
base64.b64encode(bytes)
```

```python

