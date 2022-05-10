import lzma
# Test LZMADecompressor
d = lzma.LZMADecompressor()
d.decompress(b"XZ\x00\x04\xe6\xd6\xb4F\x02\x00\x21\x01\x16\x00\x00\x00")

# Test LZMAFile
with lzma.open(BytesIO(b"XZ\x00\x04\xe6\xd6\xb4F\x02\x00\x21\x01\x16\x00\x00\x00")) as f:
    f.read()
    f.seek(0)
    f.read()
    f.seek(0)
    f.read()
    f.seek(0)
    f.read()
    f.seek(0)
    f.read()
    f.seek(0)
    f.read()
    f.seek(0)
    f.read()
    f.seek(0)
    f.read()
    f.seek(0)
    f.read()
    f.
