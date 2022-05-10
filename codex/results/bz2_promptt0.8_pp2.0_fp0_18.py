import bz2
# Test BZ2Decompressor
bz2c = bz2.BZ2Compressor(9)
bz2c.compress(b'hello world')

bz2c.flush(bz2.BZ_FINISH)

bz2c.compress(b'hello world')

bz2c.flush()

bz2d = bz2.BZ2Decompressor()
data = bz2d.decompress(bz2c.flush())
data

bz2d.decompress(b'BZh91AY&SY?>\x1c\x8d\x0e\r\r(\x02\x01\x0e\n')

bz2d.decompress(b'BZh91AY\xd2\x88\xcd\x02\xc9\x0c\x96\x8f\x07\x06\xe6\x99\x04\x10\x9f\x0f\x05\x00\x00\x00\t\x81\x0b
