import lzma
# Test LZMADecompressor for each of the
# FILESIZE_TO_TEST_BYTES chunks in compressed_file_name
with open(compressed_file_name, 'rb') as compressed_file:
    decompressor = lzma.LZMADecompressor()
    while True:
        chunk_header = compressed_file.read(5)
        if len(chunk_header) == 0:
            break
        # Get the chunk size from the header
        chunk_size, = struct.unpack('<I', chunk_header[1:])
        # Read the chunk data
        chunk_data = compressed_file.read(chunk_size)
        # Decompress the data
        decompressed_data = decompressor.decompress(chunk_data)
        # Check that the decompressed data is the same
        # as the original data
        original_data = uncompressed_file_data[decompressor.unused_data_offset:
                                               decompressor.unused_data_offset + len(decompressed_data)]
        if decompressed_data != original_data:
