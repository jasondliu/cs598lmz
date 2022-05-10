from lzma import LZMADecompressor
LZMADecompressor.decompress(data)
# b'This is the text to be compressed. '

# The decompressor object can be used to decompress multiple streams
decompressor = LZMADecompressor()
decompressor.decompress(data)
# b'This is the text to be compressed. '
decompressor.decompress(data)
# b'This is the text to be compressed. '

# LZMADecompressor supports incremental decompression
decompressor = LZMADecompressor()
decompressor.decompress(data[:5])
# b''
decompressor.decompress(data[5:])
# b'This is the text to be compressed. '

# The decompressor object can be used as a context manager
# to automatically finish the decompression process
with LZMADecompressor() as decompressor:
    decompressor.decompress(data)
    # b'This is the text to be compressed. '
```

```python
# lzma.open() can be used to read compressed files
with l
