import bz2
bz2.decompress(data)

# Writing compressed files

with open('compress.bz2', 'wb') as fout:
    f_c = bz2.BZ2File(fout, 'w')
    f_c.write(data)
    f_c.close()

# Compressing data streams

f_c = bz2.BZ2Compressor()
with open('compress.bz2', 'wb') as fout:
    fout.write(f_c.compress(data))
    fout.write(f_c.flush())

f_c = bz2.BZ2Compressor()
with open('compress.bz2', 'wb') as fout:
    for chunk in chunks:
        fout.write(f_c.compress(chunk))
    fout.write(f_c.flush())

# Decompressing data streams

f_c = bz2.BZ2Decompressor()
with open('compress.bz2', 'rb') as fin:

