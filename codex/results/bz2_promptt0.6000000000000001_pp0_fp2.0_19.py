import bz2
# Test BZ2Decompressor with multiple input streams
# Not using a file, as that would require a file that is compressed with bz2,
# and the file compression is different than the stream compression.
d = bz2.BZ2Decompressor()
data = d.decompress(b"1" * 100000)
d = bz2.BZ2Decompressor()
data += d.decompress(b"2" * 100000)
print(data)

# Test BZ2Compressor with multiple input streams
c = bz2.BZ2Compressor()
data = c.compress(b"hello")
data += c.compress(b"world")
data += c.flush()
print(data)

# Test BZ2Compressor with multiple input streams
c = bz2.BZ2Compressor()
data = c.compress(b"hello")
data += c.compress(b"world")
data += c.flush()
print(data)

# Test BZ2Decompressor with multiple input streams
d = bz2.BZ2Decompressor
