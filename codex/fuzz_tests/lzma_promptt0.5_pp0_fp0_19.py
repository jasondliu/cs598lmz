import lzma
# Test LZMADecompressor

with open("samples/sample_lzma.xz", "rb") as f:
    lzma_data = f.read()

with lzma.open("samples/sample_lzma.xz") as f:
    lzma_data_xz = f.read()

assert lzma_data == lzma_data_xz

# Test LZMACompressor

with open("samples/sample_lzma.xz", "rb") as f:
    lzma_data = f.read()

compressor = lzma.LZMACompressor()

data = b"hello world"

compressed = compressor.compress(data)
compressed += compressor.flush()

assert lzma_data == compressed
 
# Test LZMADecompressor with multiple .xz files

with open("samples/sample_lzma.xz", "rb") as f:
    lzma_data = f.read()

with open("samples/sample_lzma2
