import lzma
# Test LZMADecompressor behavior when the input file is missing EOF marker.
# It should raise an exception.

# Create a file with an invalid LZMA stream.
with open("test.lzma", "wb") as file:
    file.write(b"\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\xFF")

