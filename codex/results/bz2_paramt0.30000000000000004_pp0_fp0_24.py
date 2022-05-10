from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(b'hello world!'))

# bz2.open()
# bz2.open() is a shortcut for BZ2File()
with bz2.open('file.txt.bz2', 'wt') as f:
    f.write('Hello World!')

with bz2.open('file.txt.bz2', 'rt') as f:
    print(f.read())

# bz2.compress()
# bz2.compress() returns the compressed data as a bytes object
data = bz2.compress(b'Hello World!')
print(data)

# bz2.decompress()
# bz2.decompress() returns the decompressed data as a bytes object
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe
