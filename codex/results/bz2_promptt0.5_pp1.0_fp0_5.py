import bz2
# Test BZ2Decompressor

bz2_data = bz2.compress(b"Hello, World!")

bz2_decompressor = bz2.BZ2Decompressor()
decompressed_data = bz2_decompressor.decompress(bz2_data)

print(decompressed_data)

# Test BZ2File

with bz2.BZ2File("compressed_file.bz2", "w") as file:
    file.write(b"Hello, World!")

with bz2.BZ2File("compressed_file.bz2", "r") as file:
    print(file.read())

# Test compress and decompress

compressed_data = bz2.compress(b"Hello, World!")

decompressed_data = bz2.decompress(compressed_data)

print(decompressed_data)
# Test compresslevel

compressed_data = bz2.compress(b"Hello, World!", compresslevel=5)

decompressed
