import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with bz2.open('file.bz2', 'rb') as input:
    with open('file.out', 'wb') as output:
        for data in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(data))

        output.write(decompressor.flush())
 
# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('file.in', 'rb') as input:
    with bz2.open('file.bz2', 'wb') as output:
        for data in iter(lambda: input.read(100 * 1024), b''):
            output.write(compressor.compress(data))

        output.write(compressor.flush())
 
# Test BZ2File

with bz2.BZ2File('file.bz2', 'r') as input:
    data = input.read()

with bz2.B
