import bz2
# Test BZ2Decompressor

with bz2.BZ2File('data/example4.bz2', 'r') as input:
    with open('data/uncompressed.txt', 'wt') as output:
        decompressor = bz2.BZ2Decompressor()
        for block in iter(lambda: input.read(100 * decompressor.decompress(b'')), b''):
            data = decompressor.decompress(block)
            output.write(data.decode('utf-8'))
 
# Test BZ2Compressor

with open('data/uncompressed.txt', 'rt') as input:
    with bz2.BZ2File('data/compressed.bz2', 'w') as output:
        compressor = bz2.BZ2Compressor()
        for line in input:
            data = line.encode('utf-8')
            while len(data) > 100:
                output.write(compressor.compress(data[:100]))
                data = data[100:]
        output.write(compressor.flush())
