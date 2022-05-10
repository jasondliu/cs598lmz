import bz2
bz2.BZ2Compressor.compress(data)

# Decompress data
bz2.BZ2Decompressor().decompress(data)

# Compress file
with bz2.BZ2File('file.bz2', 'w') as f:
    f.write(data)

# Decompress file
with bz2.BZ2File('file.bz2', 'r') as f:
    data = f.read()
```

# Zlib

```py
import zlib

# Compress data
zlib.compress(data)

# Decompress data
zlib.decompress(data)
```

# References

1. [Python3 Compression and Archiving](https://www.devdungeon.com/content/python3-compression-and-archiving)
