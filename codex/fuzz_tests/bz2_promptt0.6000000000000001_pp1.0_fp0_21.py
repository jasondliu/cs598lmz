import bz2
# Test BZ2Decompressor
bz2_compressor = bz2.BZ2Compressor()
bz2_data = bz2_compressor.compress(data)
bz2_data += bz2_compressor.flush()
len(bz2_data)

bz2_decompressor = bz2.BZ2Decompressor()
uncompressed_data = bz2_decompressor.decompress(bz2_data)
len(uncompressed_data)

# Test BZ2File
with bz2.BZ2File('compressed_file.bz2', 'wb') as writer:
    writer.write(data)

with bz2.BZ2File('compressed_file.bz2', 'rb') as reader:
    uncompressed_data = reader.read()
    len(uncompressed_data)
