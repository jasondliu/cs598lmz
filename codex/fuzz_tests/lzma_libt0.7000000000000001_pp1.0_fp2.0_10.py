import lzma
lzma.LZMAFile(fileobj=strm).read(10)

# write a new file
with open('test.lzma', 'wb') as f:
    c = lzma.LZMACompressor()
    f.write(c.compress(b'hello world'))
    f.write(c.flush())

# read the file again
with open('test.lzma', 'rb') as f:
    d = lzma.LZMADecompressor()
    print(d.decompress(f.read()))

# write a new file
with lzma.open('test.xz', 'wb') as f:
    f.write(b'hello world')

# read the file
with lzma.open('test.xz', 'rb') as f:
    print(f.read())

# get the uncompressed size
with lzma.open('test.xz', 'rb') as f:
    print(f.seek(0, io.SEEK_END))
