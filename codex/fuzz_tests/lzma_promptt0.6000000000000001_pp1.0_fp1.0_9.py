import lzma
# Test LZMADecompressor
comp = lzma.LZMADecompressor()
comp.decompress(b"\x00\x00\x80\x00\xfd\xff\xff\xff")

# Test LZMACompressor
f = io.BytesIO()
cmp = lzma.LZMACompressor()
cmp.compress(b"foo")
cmp.flush(lzma.RUN)
cmp.compress(b"bar")
cmp.flush()
cmp.compress(b"baz")
cmp.flush()

with lzma.open(f, "r") as fin:
    fin.read()

with lzma.open(f, "w") as fout:
    fout.write(b"foo")
    fout.flush(lzma.RUN)
    fout.write(b"bar")
    fout.flush()
    fout.write(b"baz")
    fout.flush()

with lzma.open(f, "w") as fout:
    fout.write
