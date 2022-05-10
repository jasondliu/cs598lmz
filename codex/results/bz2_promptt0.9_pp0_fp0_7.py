import bz2
# Test BZ2Decompressor
bz_comp = bz2.BZ2Compressor()
uncompressed_data = b'This is some uncompressed data that we want to compress by using BZ2Compressor'

compressed_data = bz_comp.compress(uncompressed_data)
print('Compressed data: ', compressed_data)

bz_decomp = bz2.BZ2Decompressor()
new_data = bz_decomp.decompress(compressed_data)
print('Again decompressed data: ', new_data)

print('Original data matches new data: ',uncompressed_data== new_data)

# Obtain exisiting compress file
with open('../../data/twitter.bz2') as twitter_in, open('../../data/uncompressed_twitter.txt', 'wb') as twitter_out:
    # Create bz2 decompressor object
    bz_decomp = bz2.BZ2Decompressor()
    # Decompress twitter.bz2 file
    for data in iter(lambda : twitter_in.read
