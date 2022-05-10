import lzma
# Test LZMADecompressor

# Open the input file
with lzma.LZMAFile("test.xz", mode="r") as f:
    # Create a new LZMADecompressor object
    decomp = lzma.LZMADecompressor()
    # Read the header from the input file
    header = f.read(31)
    # Tell the decompressor about the header
    decomp.header = header
    # Read the rest of the stream
    data = f.read()

    # Decompress the data
    uncompressed_data = decomp.decompress(data)
    print(uncompressed_data)
    # ...
    # The data is now decompressed. It can be used as a byte string,
    # written to a file, etc.
    # ...
 
# ...
# The header has to be saved if the data is needed later.


# Create a new LZMADecompressor object
decomp = lzma.LZMADecompressor()
# Tell the decompressor about the header
decomp.header = header
# Decompress the
