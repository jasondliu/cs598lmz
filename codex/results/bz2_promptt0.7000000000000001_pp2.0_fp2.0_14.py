import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()

# Read one compressed chunk (256 bytes by default)
chunk = fileobj.read(512)

# Pass the chunk to the decompressor object
decompressed_data = decompressor.decompress(chunk)

# Decompress the rest of the file
for chunk in iter(lambda: fileobj.read(512), b''):
    decompressed_data += decompressor.decompress(chunk)

# The file is fully decompressed now
# Use decompressed_data
```

## zlib

> zlib是一种压缩算法，与gzip和bzip2是同类型的，不过zlib更快一些，gzip和bzip2更压缩率更高一些。

> zlib是一个开源的、通用的压缩
