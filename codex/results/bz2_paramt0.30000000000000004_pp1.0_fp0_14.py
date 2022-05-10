from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(b'hello world!'))

# bz2.open()
with bz2.open('file.bz2', mode='wt') as f:
    f.write('contents go here')

with bz2.open('file.bz2', mode='rt') as f:
    text = f.read()

# zlib.compress()
s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
len(t)

zlib.decompress(t)

zlib.crc32(s)

# zlib.compressobj()
compressobj = zlib.compressobj(zlib.Z_DEFAULT_COMPRESSION,
                               zlib.DEFLATED,
                               -zlib.MAX_WBITS,
                               zlib.DEF_MEM_LEVEL,
                               0)

compressed = compressobj.compress(data)
compressed += compressobj.flush()

