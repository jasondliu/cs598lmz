from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh91AY&SY\xc0\x00\x00\x00\x80\x00\x0c\x80\x08\x00\x00\x00!\x88M\x03\x00\x00\x00\x01')

# b'Hello world'
```

Compressing a file in chunks:
```python
import bz2
with open('huge_file', 'rb') as orig_file:
    with bz2.open('huge_file.bz2', 'wb') as compressed_file:
        compressed_file.write(orig_file.read(1000))
```

Decompressing a file in chunks:
```python
import bz2
with bz2.open('huge_file.bz2', 'rb') as compressed_file:
    with open('huge_file', 'wb') as orig_file:
        orig_file.write(compressed_file.read(1000))
```

## Caveats

* The `BZ2File`
