import lzma
# Test LZMADecompressor

# Make random data
size = 100000
data = os.urandom(size)

# Compress with LZMA
compressor = lzma.LZMACompressor()
compressed = compressor.compress(data)
compressed += compressor.flush()

# Decompress with LZMADecompressor
decompressor = lzma.LZMADecompressor()
output = decompressor.decompress(compressed)

# Check that the output is the same as the input
if data != output:
    print("Decompressor failed?")
    print("Input and output data differ")
    sys.exit(1)
# Test that LZMADecompressor is a context manager

with lzma.LZMADecompressor() as decompressor:
    output = decompressor.decompress(compressed)

# Check that the output is the same as the input
if data != output:
    print("Decompressor failed?")
    print("Input and output data differ")
    sys.exit(1)
# Test that LZM
