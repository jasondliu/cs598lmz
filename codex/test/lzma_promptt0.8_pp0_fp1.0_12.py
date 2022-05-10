import lzma
# Test LZMADecompressor

# Open the input file
with lzma.LZMAFile("test.xz", mode="r") as f:
    # Create a new LZMADecompressor object
    decomp = lzma.LZMADecompressor()
    # Read the header from the input file
    header = f.read(31)
    # Tell the decompressor about the header
