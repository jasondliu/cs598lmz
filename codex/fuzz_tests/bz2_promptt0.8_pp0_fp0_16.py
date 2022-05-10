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

decomp.unconsumed_tail

decomp.decompress(b'BZh91AY&SY')

decomp.decompress('BZh91AY&SY')

b'BZh91AY&SY'.decode('utf-8')

decomp.decompress(b'BZh91AY&SY').decode('utf-8')

bz2.decompress(b'BZh91AY&SY')
# Compression
comp = bz2.BZ2Compressor()

temp = comp.compress(b'BZh91AY&SY')

temp


