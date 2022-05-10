import lzma
# Test LZMADecompressor.
d = lzma.LZMADecompressor()
with open('c:\\t.xz', 'rb') as f:
    decompressed_data = d.decompress(f.read())
</code>

