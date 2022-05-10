import lzma
# Test LZMADecompressor in block mode.
dc = lzma.LZMADecompressor()
compressed = b"xA7kRA"
decompressed = dc.decompress(compressed)
# Test LZMADecompressor in streamed mode.
dc = lzma.LZMADecompressor()
with open(__file__, "rb") as f:
    for block in iter(lambda: f.read(64), b""):
        decompressed = dc.decompress(compressed)
# Test LZMADecompressor with an empty bytes object
dc = lzma.LZMADecompressor()
decompressed = dc.decompress(b"")

import lzma
# Check LZMADecompressor.eof
data = lzma.LZMADecompressor().decompress(b"x\x9cK\xcb\xcf\x07\x00\x02\xe5")
assert lzma.LZMADecompressor().eof

import lzma
# Test lz
