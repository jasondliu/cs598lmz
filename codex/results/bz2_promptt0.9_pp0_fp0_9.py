import bz2
# Test BZ2Decompressor()
decomp = bz2.BZ2Decompressor()
res = ""
with open("small.bz2", "rb") as f:
    while True:
        res += decomp.decompress(f.read(10))
        if len(res) >= 4:
            break
# The file contains 442 lines of content, expect the last line to be only 441
# characters long (no newline character)
print("Num lines: {}, Last line length: {}".format(len(res.split("\n")), len(res.split("\n")[-1])))

# Test bz2.decompress() for all files
print("Correct file:")
with bz2.BZ2File("large.bz2", "rb") as f:
    print(f.read(2048))

# This is a bzip2 file; however, it is not valid bzip2 data. The file is
# decompressed with bz2.decompress() entirely. This is the error message
# returned by bz2.decompress()
print("
