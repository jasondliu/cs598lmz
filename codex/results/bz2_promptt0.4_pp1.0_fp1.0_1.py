import bz2
# Test BZ2Decompressor

# Create a decompressor object
decompressor = bz2.BZ2Decompressor()

# Decompress a one-shot string
original_data = decompressor.decompress(compressed_data)

# Decompress streams
with open('bzipped_file.bz2', 'rb') as f_in, open('uncompressed_file', 'wb') as f_out:
    for data in iter(lambda: f_in.read(100 * 1024), b''):
        f_out.write(decompressor.decompress(data))

# Decompress and then compress again
with open('bzipped_file.bz2', 'rb') as f_in, open('recompressed_file.bz2', 'wb') as f_out:
    decompressor = bz2.BZ2Decompressor()
    compressor = bz2.BZ2Compressor()
    for data in iter(lambda: f_in.read(100 * 1024), b''):
        f_out.write(compressor.compress(dec
