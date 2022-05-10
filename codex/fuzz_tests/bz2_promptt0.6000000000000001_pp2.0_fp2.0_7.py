import bz2
# Test BZ2Decompressor

data = bz2.compress(b'hello world')

d = bz2.BZ2Decompressor()
d.decompress(data)

d.decompress(b'BZh91AY&SY')

d.decompress(b'BZh91AY&SY')
d.flush()

d.decompress(b'BZh91AY&SY')
d.flush()

d.decompress(b'BZh91AY&SY')
d.flush()
