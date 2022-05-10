import bz2
# Test BZ2Decompressor with a file containing incomplete streams.
# The output should be the concatenation of all the content of the complete
# streams.

test_file = bz2.BZ2File(findfile("issue23278.in.bz2"))
bz2_decompressor = bz2.BZ2Decompressor()
decompressed_file = ""
while True:
    block = test_file.read(100)
    if not block:
        break
    decompressed_file += bz2_decompressor.decompress(block)

with open(findfile("issue23278.in"), "rb") as expected_file:
    if decompressed_file != expected_file.read():
        raise AssertionError("Concatenation of the decompressed content"
                             "is not equal to original file")
