import bz2
# Test BZ2Decompressor
bz2_decompressor = bz2.BZ2Decompressor()

try:
    decompressed_data = bz2_decompressor.decompress(compressed_data)
    print(decompressed_data)
except EOFError:
    print("End of file")

# When done, dispose of the compression object to release its buffers and resources
bz2_decompressor.close()

"""
Step 2: using the context manager
"""
with bz2.BZ2Compressor() as compressor:
    compressed_data = compressor.compress(data)
    compressed_data += compressor.flush()

with bz2.BZ2Decompressor() as decompressor:
    try:
        decompressed_data = decompressor.decompress(compressed_data)
        print(decompressed_data)
    except EOFError:
        print("End of file")

"""
Step 3: using the built-in functions
"""
compressor = bz2.compress(data)
decompressor = bz2.decomp
