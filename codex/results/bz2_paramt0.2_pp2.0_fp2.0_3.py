from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(b'hello world!'))

# bz2.open()
with bz2.open('file.bz2', 'wt') as f:
    f.write('contents go here')

with bz2.open('file.bz2', 'rt') as f:
    text = f.read()

# bz2.compress()
data = bz2.compress(b'hello world!')
print(data)

# bz2.decompress()
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print(bz2.decompress(data))

# bz2.BZ2Compressor()
compressor = bz2.BZ2Compressor()
print(
