import lzma
# Test LZMADecompressor
import lzma

# See https://docs.python.org/3/library/lzma.html
# See https://stackoverflow.com/questions/27884312/python-lzma-extract-method-not-working

# The file we want to decompress
file_to_decompress = "../../data/compressed_data/test_lzma.xz"

# Open the file in read binary mode
with open(file_to_decompress, "rb") as input:
    # Create a decompressor object
    decompressor = lzma.LZMADecompressor()
    # Read the entire file. We need this to decompress it in one shot
    data = input.read()
    # Decompress the entire file
    uncompressed_data = decompressor.decompress(data)
    # Show the result
    print(uncompressed_data)

# Test LZMADecompressor
import lzma

# See https://docs.python.org/3/library/lzma.html
#
