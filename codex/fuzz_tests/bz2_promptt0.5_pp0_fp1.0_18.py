import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open("example.bz2", "rb") as input:
    with open("example.out", "wb") as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(block))
        output.write(decompressor.flush())
import bz2

compressor = bz2.BZ2Compressor()

with open("example.out", "rb") as input:
    with open("example.bz2", "wb") as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(compressor.compress(block))
        output.write(compressor.flush())
 
import bz2

with bz2.open("example.bz2", "rb") as input:
    with open("example.out", "wb") as output:
        output.write(input.read())
 
import bz2


