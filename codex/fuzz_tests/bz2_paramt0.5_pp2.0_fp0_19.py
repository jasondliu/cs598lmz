from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# decompress a file
with open('file.txt.bz2', 'rb') as f:
    file_content = f.read()
    uncompressed_data = BZ2Decompressor().decompress(file_content)
    print(uncompressed_data)

# compress data
data = b'Lots of data here.'
compressor = BZ2Compressor()
compressor.compress(data)
compressor.flush()
compressed_data = compressor.compress(data)

# compress a file
with open('file.txt', 'rb') as f:
    data = f.read()
    compressor = BZ2Compressor()
    compressed_data = compressor.compress(data)
    compressed_data += compressor.flush()

with open('file.txt.bz2', 'wb') as f:
    f.write(compressed_data)

# compress a file without the flush
with open('file.txt', 'rb') as input:
    with open('file.txt.bz
