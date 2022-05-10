import bz2
# Test BZ2Decompressor with a stream that has multiple concatenated bz2 streams

TEST_FILE = "test/data/sample1.bz2"

# Read the whole file, decompress it, and check that the result is as expected.
with open(TEST_FILE, "rb") as input:
    decompressor = bz2.BZ2Decompressor()
    data = input.read(100)
    while data:
        output = decompressor.decompress(data)
        print(output)
        data = input.read(100)
    output = decompressor.flush()
    print(output)
