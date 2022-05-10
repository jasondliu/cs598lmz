import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with bz2.open('example.bz2', 'rb') as input:
    with open('example.out', 'wb') as output:
        while True:
            block = input.read(100)
            if not block:
                break
            output.write(decompressor.decompress(block))

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('example.out', 'rb') as input:
    with bz2.open('example.bz2', 'wb') as output:
        while True:
            block = input.read(100)
            if not block:
                break
            output.write(compressor.compress(block))
        output.write(compressor.flush())
 
# Test BZ2File

with bz2.open('example.bz2', 'rb') as input:
    with open('example.out', 'wb') as output:
        while True:
            block =
