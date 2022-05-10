import lzma
# Test LZMADecompressor
c = lzma.LZMACompressor()
data = b"Lots of data." * 10**6
compressed = c.compress(data)
compressed += c.flush()
len(compressed)

d = lzma.LZMADecompressor()
# No way to know how big the output will be, so we must specify an upper bound
uncompressed = d.decompress(compressed, 10**9 + 1)
len(uncompressed)

uncompressed == data

# The LZMADecompressor class can also be used as a context manager
with lzma.LZMADecompressor() as d:
    uncompressed = d.decompress(compressed, 10**9 + 1)
    len(uncompressed)
```

```
>>> import lzma
>>> f = open("/tmp/foo.xz", "wb")
>>> with lzma.LZMACompressor(format=lzma.FORMAT_XZ) as c:
...     f.write(c.compress(
