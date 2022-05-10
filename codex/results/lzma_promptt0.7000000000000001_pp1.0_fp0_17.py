import lzma
# Test LZMADecompressor
decomp = lzma.LZMADecompressor()

with open("compressed_file.xz", 'rb') as f:
    file_content = f.read()
    decompressed_data = decomp.decompress(file_content)
    print(decompressed_data)

with open("decompressed_file", 'w') as f:
    f.write(decompressed_data.decode("utf-8"))

with open("decompressed_file", 'r') as f:
    print(f.read())

# Test LZMACompressor
comp = lzma.LZMACompressor()

with open("regular_file", 'r') as f:
    data = f.read()
    compressed_data = comp.compress(data.encode("utf-8"))
    compressed_data += comp.flush()

with open("compressed_file.xz", 'wb') as f:
    f.write(compressed_data)

with open("compressed_file.xz", 'rb') as f
