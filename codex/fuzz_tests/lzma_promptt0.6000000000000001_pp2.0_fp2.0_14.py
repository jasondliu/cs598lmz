import lzma
# Test LZMADecompressor

# Read the test file
with open('lzma_compressed.dat', 'rb') as input:
    try:
        decompressor = lzma.LZMADecompressor()
        # Read the header
        header = input.read(5)
        decompressor.decompress(header)
        # Read the compressed data
        data = input.read()
        # Decompress
        result = decompressor.decompress(data)
    except lzma.LZMAError as e:
        print("Decompression failed: {}".format(e))

print(result)

# Check if the result is correct
with open('lzma_uncompressed.dat', 'rb') as ref:
    ref_data = ref.read()

print(ref_data == result)

# Test LZMADecompressor with one-shot method

with open('lzma_compressed.dat', 'rb') as input:
    try:
        # Read the header
        header = input.read(5)
        # Read the compressed data

