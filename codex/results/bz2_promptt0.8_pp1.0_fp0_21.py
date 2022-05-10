import bz2
# Test BZ2Decompressor

# BZ2Decompressor
dec = bz2.BZ2Decompressor()
dec_source = 'Надо открыть файл методом BZ2.decompress(data)'
decompressed = dec.decompress(bz2.compress(dec_source.encode()))
print(decompressed.decode())

# use with open
decompressed_file = open('BZ2.txt.bz2', 'rb')
dec = bz2.BZ2Decompressor()
decompressed = dec.decompress(decompressed_file.read())
print(decompressed.decode())

# test blocks
dec_source = 'Надо открыть файл методом BZ2.decompress(data)'
decompressed = dec.decompress(bz2.compress(dec_source.encode()))
print(decompressed.
