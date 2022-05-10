from lzma import LZMADecompressor
LZMADecompressor().decompress(lzma_data)

# b'Hello World!'
```

## lzma.LZMACompressor

```python
import lzma

compressor = lzma.LZMACompressor()
data = b'Hello World!'
compressed = compressor.compress(data)
compressed += compressor.flush()

print(compressed)
# b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xcaMU\xe5\x02\x00\x00\x00\x00\x04\xe6\xd6\xb4F'
```

## lzma.LZMADecompressor

```python
import lzma

compressor = lzma.LZMACompressor()
data = b'Hello World!'
compressed = compressor.compress(data)
compressed += compressor.flush()

decomp
