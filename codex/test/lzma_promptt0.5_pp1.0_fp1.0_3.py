import lzma
# Test LZMADecompressor with a large block size.

data = b'\x00' * 1024 * 1024

# Create a large input file.
with open('lzma_large_decompressor_input', 'wb') as f:
    f.write(data)

# Compress it.
with open('lzma_large_decompressor_input', 'rb') as f:
    with open('lzma_large_decompressor_output', 'wb') as f2:
        lzc = lzma.LZMACompressor()
        while True:
            block = f.read(1024 * 1024)
            if not block:
                break
            f2.write(lzc.compress(block))
        f2.write(lzc.flush())

# Decompress the compressed data.
