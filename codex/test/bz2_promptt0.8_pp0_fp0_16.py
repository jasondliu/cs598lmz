import bz2
# Test BZ2Decompressor
with bz2.BZ2File('file.bz2') as f:
    data = f.read()


# Test BZ2Compressor
with bz2.BZ2File('file.bz2', 'w') as f:
    f.write(data)

print
# Decompression
decomp=bz2.BZ2Decompressor()
type(decomp)

decomp.eof

