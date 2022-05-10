import bz2
bz2c = bz2.BZ2Compressor(9)
bz2c.compress(b'A')
bz2c.compress(b'bcd')
bz2c.flush()

bz2d = bz2.BZ2Decompressor()
bz2d.decompress(bz2c.compress(b'A'))
bz2d.decompress(bz2c.compress(b'bcd'))
bz2d.decompress(bz2c.flush())

bz2.decompress(bz2.compress(b'hello world'))

for x in range(10):
    if bz2.compress(b'hello world') != bz2.compress(b'hello world'):
        print(x)

bz2c = bz2.BZ2Compressor(9)
bz2c.compress(b'A' * 1000)
bz2c.flush(2)
bz2c.compress(b'B
