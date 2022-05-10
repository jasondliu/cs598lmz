import lzma
# Test LZMADecompressor

lzc = lzma.LZMADecompressor()

with open("lzma_test.xz", "rb") as f:
    file_content = f.read()

decompressed_data = lzc.decompress(file_content)

with open("lzma_test_decompressed.txt", "wb") as f:
    f.write(decompressed_data)

print("Decompression complete")

# Test LZMACompressor

lzc = lzma.LZMACompressor()

with open("lzma_test_decompressed.txt", "rb") as f:
    file_content = f.read()

compressed_data = lzc.compress(file_content)

with open("lzma_test_compressed.xz", "wb") as f:
    f.write(compressed_data)

print("Compression complete")

# Test LZMAFile

with lzma.open("lzma_test.xz")
