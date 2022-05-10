from lzma import LZMADecompressor
LZMADecompressor()

# The compressed data is a byte array
compressed = b'...'

# Decompress the data
decompressed = LZMADecompressor().decompress(compressed)

# The variable 'decompressed' contains the decompressed data
# ...

# When the compressed data is no longer needed, call flush() to free up memory
LZMADecompressor().flush()
```

## Multithreading

The `LZMADecompressor` class is thread-safe. Each thread must create its own
instance of `LZMADecompressor`.

## Compression format

The compression format used by lzma is the same used by 7-Zip, XZ Utils, and
PPMd. For more details, see [XZ Utils
documentation](http://tukaani.org/xz/xz-file-format.txt).
