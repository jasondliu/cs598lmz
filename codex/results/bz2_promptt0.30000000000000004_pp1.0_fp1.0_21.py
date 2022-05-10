import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('sample.bz2', 'rb') as f_compressed:
    # Read a chunk of compressed data
    chunk = f_compressed.read(100)
    # Decompress the chunk and print the result
    print(decompressor.decompress(chunk))
    # Read the next chunk
    chunk = f_compressed.read(100)
    # Finish decompression
    print(decompressor.decompress(chunk, finish=True))

# Decompress data with BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('sample.bz2', 'rb') as f_compressed:
    with open('sample.txt', 'wb') as f_decompressed:
        for data in iter(lambda: f_compressed.read(100 * 1024), b''):
            f_decompressed.write(decompressor.decompress(data))

# Compress data with BZ2Compressor
