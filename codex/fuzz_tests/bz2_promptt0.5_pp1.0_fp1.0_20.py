import bz2
# Test BZ2Decompressor
bz_decompressor = bz2.BZ2Decompressor()
uncompressed_data = bz_decompressor.decompress(compressed_data)
uncompressed_data

# Test BZ2File
print("Reading from compressed file:")
with bz2.BZ2File("example_file.bz2", "rb") as input:
    print(input.readline())
print("\nReading from uncompressed file:")
with open("example_file.txt", "rt") as input:
    print(input.readline())

# Compress data
data = b"Lots of content here"
with bz2.BZ2File("example_file.bz2", "wb") as output:
    output.write(data)

# Compress data incrementally
with bz2.BZ2File("example_file.bz2", "wb") as output:
    for i in range(10):
        output.write(data)


# Compress data using a compressor object
compressor = bz2.BZ2
