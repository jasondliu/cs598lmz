import bz2
bz2.BZ2Compressor()

# decompress
bz2.BZ2Decompressor()

# compress data
bz2.compress(data)

# decompress data
bz2.decompress(data)

# open compressed file
bz2.BZ2File(filename)

# open for reading
bz2.BZ2File(filename, 'r')

# open for writing
bz2.BZ2File(filename, 'w')

# open for appending
bz2.BZ2File(filename, 'a')
```

## lzma

```python
import lzma

# compress
lzma.LZMACompressor()

# decompress
lzma.LZMADecompressor()

# compress data
lzma.compress(data)

# decompress data
lzma.decompress(data)

# open compressed file
lzma.LZMAFile(filename)

# open for reading
lzma.LZMAFile
