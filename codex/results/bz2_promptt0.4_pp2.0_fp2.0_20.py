import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed_data)
 
# Test BZ2File
with bz2.BZ2File('file.bz2', 'wb') as f:
    f.write(data)

with bz2.BZ2File('file.bz2', 'rb') as f:
    file_content = f.read()

file_content == data
 
# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
compressor.compress(data)
compressor.flush()
 
# Test BZ2File
with bz2.BZ2File('file.bz2', 'wb') as f:
    f.write(data)

with bz2.BZ2File('file.bz2', 'rb') as f:
    file_content = f.read()

file_content == data
 
# Test BZ2Compressor
compressor = bz2.BZ2Compressor()

