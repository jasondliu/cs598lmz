import bz2
# Test BZ2Decompressor
# decompressor = bz2.BZ2Decompressor()
# with open('/Users/matthew/Documents/Python/Python-for-Everybody/Using Python to Access Web Data/sampletext.bz2', 'rb') as input:
#     for block in iter(lambda: input.read(100 * decompressor.decompress_block_size), b''):
#         print(decompressor.decompress(block))

# Test BZ2Compressor
# compressor = bz2.BZ2Compressor()
# with open('/Users/matthew/Documents/Python/Python-for-Everybody/Using Python to Access Web Data/sampletext.bz2', 'wb') as output:
#     for data in ['The first line goes here.\n', 'And the second line goes here.\n']:
#         output.write(compressor.compress(data))
#     output.write(compressor.flush())

# Test BZ2File
# with bz2.BZ2File('/Users/matthew/Documents/Python/Python-
