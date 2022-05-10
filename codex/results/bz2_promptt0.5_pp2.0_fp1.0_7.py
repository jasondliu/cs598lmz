import bz2
# Test BZ2Decompressor

bz2_decompressor = bz2.BZ2Decompressor()
uncompressed_data = bz2_decompressor.decompress(compressed_data)
uncompressed_data

# Test BZ2File

with bz2.BZ2File('data/compressed_file.bz2', 'rb') as bz2_file:
    uncompressed_data = bz2_file.read()
uncompressed_data
 
 
# Compress file with bz2

with open('data/file_to_compress.txt', 'rb') as f_in, \
     bz2.BZ2File('data/compressed_file.bz2', 'wb') as f_out:
    f_out.writelines(f_in)
 
 
# Uncompress file with bz2

with bz2.BZ2File('data/compressed_file.bz2', 'rb') as f_in, \
     open('data/uncompressed_file.txt', 'wb
