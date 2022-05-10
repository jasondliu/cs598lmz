import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()

with open("data/bzipped_file.bz2", "rb") as f:
    file_content = f.read()

print(decompressor.decompress(file_content))

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
uncompressed_data = b"This is uncompressed data."
compressed_data = compressor.compress(uncompressed_data)

print(compressed_data)

# Test BZ2File
with bz2.BZ2File("data/compressed_file.bz2", "wb") as f:
    f.write(uncompressed_data)

with bz2.BZ2File("data/compressed_file.bz2", "rb") as f:
    print(f.read())

with bz2.BZ2File("data/compressed_file.bz2", "rb") as f_in, open("data/uncompressed_file.txt
