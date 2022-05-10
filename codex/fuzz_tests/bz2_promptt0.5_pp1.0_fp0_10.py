import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed_data)

# Test BZ2File
uncompressed_file = bz2.BZ2File('uncompressed.txt', 'wb')
uncompressed_file.write(compressed_data)
uncompressed_file.close()

# Compress a file
bz2_compressor = bz2.BZ2Compressor()
input_file = open('lorem.txt', 'rb')
try:
    while True:
        block = input_file.read(1024)
        if not block:
            break
        compressed_data = bz2_compressor.compress(block)
        if compressed_data:
            output_file.write(compressed_data)
    # Flush the compressor because we are done
    remaining_data = bz2_compressor.flush()
    output_file.write(remaining_data)
finally:
    input_file.close()
    output_file.close()

# Dec
