from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# bz2.open()
with bz2.open('file.bz2', 'rt') as f:
    data = f.read()

with bz2.open('file.bz2', 'wt') as f:
    f.write(data)

with bz2.open('file.bz2', 'rt') as input, \
     gzip.open('file.gz', 'wt') as output:
    for line in input:
        output.write(line)

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
                
