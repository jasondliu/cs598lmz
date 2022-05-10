import bz2
# Test BZ2Decompressor

bz_decompressor = bz2.BZ2Decompressor()

uncompressed_data = bz_decompressor.decompress(compressed_data)

uncompressed_data == original_data
# Test BZ2File

bz2_file = bz2.BZ2File('file.bz2', 'wb')
bz2_file.write(original_data)
bz2_file.close()

bz2_file = bz2.BZ2File('file.bz2', 'rb')
uncompressed_data = bz2_file.read()
bz2_file.close()

uncompressed_data == original_data
 
# Test BZ2File with context manager

with bz2.BZ2File('file.bz2', 'wb') as bz2_file:
    bz2_file.write(original_data)

with bz2.BZ2File('file.bz2', 'rb') as bz2_file:
    uncomp
