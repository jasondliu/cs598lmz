import bz2
# Test BZ2Decompressor

# BZ2Decompressor
dec = bz2.BZ2Decompressor()
dec_source = 'Надо открыть файл методом BZ2.decompress(data)'
decompressed = dec.decompress(bz2.compress(dec_source.encode()))
print(decompressed.decode())

# use with open
