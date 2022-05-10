import bz2
# Test BZ2Decompressor object
decompressor = bz2.BZ2Decompressor()

fd = open('../../data/bzip_data/sample.bz2', 'rb')

try:
    for block in iter(lambda : fd.read(100 * decompressor.decompress_blockSize), b''):
        decompressed_data = decompressor.decompress(block)
        print(decompressed_data)
finally:
    fd.close()

# Test BZ2File
fd = bz2.BZ2File('../../data/bzip_data/sample.bz2')
for line in fd:
    print(line)
fd.close()

# Test BZ2Compressor object
compressor = bz2.BZ2Compressor()

fd = open('../../data/bzip_data/sample.bz2', 'wb')

try:
    for data in ['The quick brown fox', 'jumps over', 'the lazy dog.']:
        compressed_data = compressor.compress(data)
        fd.
