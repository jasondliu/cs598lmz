import lzma
# Test LZMADecompressor with streamed data

data = b'x' * 10
compress = lzma.LZMACompressor()

compressed = compress.compress(data) + compress.flush()
decompress = lzma.LZMADecompressor()

decompressed = decompress.decompress(compressed)
print(len(decompressed) == len(data))

# Test LZMADecompressor with multiple calls

data = b'x' * 10
compress = lzma.LZMACompressor()

compressed = compress.compress(data) + compress.flush()
decompress = lzma.LZMADecompressor()

decompressed = b''
index = 0
while index < len(compressed):
    slice = compressed[index:index + 1024]
    decompressed += decompress.decompress(slice)
    index += 1024
print(len(decompressed) == len(data))
