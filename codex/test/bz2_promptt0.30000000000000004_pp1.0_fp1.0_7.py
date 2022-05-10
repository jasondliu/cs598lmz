import bz2
# Test BZ2Decompressor
with open("test.bz2", "rb") as input:
    decompressor = bz2.BZ2Decompressor()
    with open("test.txt", "wb") as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(block))
