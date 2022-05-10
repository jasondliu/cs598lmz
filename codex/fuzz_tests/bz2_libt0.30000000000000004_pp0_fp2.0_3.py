import bz2
bz2.decompress(data)

# bz2.BZ2Decompressor()
d = bz2.BZ2Decompressor()
d.decompress(data)
d.decompress(data)

# bz2.open()
with bz2.open('file.bz2', 'wt') as f:
    f.write('Hello World')

with bz2.open('file.bz2', 'rt') as f:
    text = f.read()

# bz2.compress()
bz2.compress(b'Hello World')

# bz2.decompress()
bz2.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# bz2.BZ2Comp
