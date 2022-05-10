import bz2
# Test BZ2Decompressor
with open("data/compressed.bz2", "rb") as f:
    decompressor = bz2.BZ2Decompressor()
    decompressed_data = decompressor.decompress(f.read())
    with open("data/decompressed.txt", "wb") as fw:
        fw.write(decompressed_data)
 
# Test BZ2Compressor
with open("data/decompressed.txt", "rb") as f:
    data = f.read()
    compressor = bz2.BZ2Compressor()
    compressed_data = compressor.compress(data)
    with open("data/compressed.bz2", "wb") as fw:
        fw.write(compressed_data)
 
# Test compress() and decompress()
with open("data/decompressed.txt", "rb") as f:
    data = f.read()
    compressed_data = bz2.compress(data)
    with open("data/compressed.bz2", "wb") as fw:

