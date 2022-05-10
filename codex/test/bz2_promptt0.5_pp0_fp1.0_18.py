import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open("example.bz2", "rb") as input:
    with open("example.out", "wb") as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(block))
