import bz2
# Test BZ2Decompressor

bz2.decompress(bz2.compress(b"Hello world"))

# Test BZ2Compressor

bz2.compress(b"Hello world")
# Test BZ2File

bz2.open(bz2.compress(b"Hello world"))
bz2.open(bz2.compress(b"Hello world"), mode="w")
bz2.open(bz2.compress(b"Hello world"), mode="r")
bz2.open(bz2.compress(b"Hello world"), mode="rb")
bz2.open(bz2.compress(b"Hello world"), mode="wb")
bz2.open(bz2.compress(b"Hello world"), mode="rt")
bz2.open(bz2.compress(b"Hello world"), mode="wt")
bz2.open(bz2.compress(b"Hello world"), mode="rt", encoding="utf-8")
bz2.open(bz2.compress(b"Hello
