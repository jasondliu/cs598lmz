import bz2
bz2.decompress(text)
 
# bz2.BZ2File
# bz2.BZ2Decompressor

text = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
bz2.decompress(text)

# bz2.open()
with bz2.open('bzipped.bz2') as f:
    text = f.read()

with bz2.open('bzipped.bz2', 'wt') as f:
    f.write(text)

# bz2.compress()
text = b'A lot of compressible data ... '
len(text)

compressed = bz2.compress(text)
len(compressed)

bz2.decompress(compressed)
