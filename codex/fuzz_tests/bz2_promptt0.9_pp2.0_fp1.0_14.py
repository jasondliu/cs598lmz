import bz2
# Test BZ2Decompressor with the whole-file API:
d = bz2.BZ2Decompressor()
with open('lorem.bz2', 'rb') as input:
    with open('lorem_copy.txt', 'wb') as output:
        while True:
            block = input.read(1024)
            if not block:
                break
            output.write(d.decompress(block))

# Test BZ2Compressor with the incremental API:
t = 'Hello, World!'
t * 128
t * 32768
t * 1000000
bz2.compress(t)
c = bz2.BZ2Compressor()
c.compress(t)
c.compress(t)
c.flush()
# compress() and decompress() also accept optional arguments for
# controlling the compression level, although the default level works
# well in most cases.
bz2.compress(t, 9)
d = bz2.decompress(bz2.compress(t, 9))
d == t
d.decode('latin-1') ==
