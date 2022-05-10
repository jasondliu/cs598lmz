import lzma
# Test LZMADecompressor
with open("test.txt.lzma", "rb") as raw_data:
    # Decompressed LZMA data
    decompressed_data = lzma.decompress(raw_data.read())
    # Check decompressed data and the original data
    assert decompressed_data == b"Hello world!\n"
    # Print decompressed data to the console
    print(decompressed_data.decode("utf-8"))

# Test LZMADecompressor
# with open("test.txt.xz", "rb") as raw_data:
#     # This will not work, because the LZMADecompressor only
#     # supports raw LZMA data, not LZMA2 data.
#     decompressed_data = lzma.decompress(raw_data.read())

# Test LZMAFile
# NOTE: This is the preferred way to decompress LZMA data.
with lzma.open("test.txt.xz") as compressed_file:
    # Read the compressed file
    compressed_data = compressed_file
