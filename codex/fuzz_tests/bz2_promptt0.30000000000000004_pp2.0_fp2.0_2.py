import bz2
# Test BZ2Decompressor

data = bz2.BZ2File('../../data/chapter3/sample.bz2', 'rb').read()
print(data)

decompressor = bz2.BZ2Decompressor()
result = decompressor.decompress(data)
print(result)

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()
result = compressor.compress(b'This is a test')
result += compressor.flush()
print(result)

# Test BZ2File

with bz2.BZ2File('../../data/chapter3/sample.bz2', 'rb') as input:
    print(input.readline())

with bz2.BZ2File('../../data/chapter3/sample.bz2', 'wb') as output:
    output.write(b'This is a test')

with bz2.BZ2File('../../data/chapter3/sample.bz2', 'rb') as input:
    print(input.readline())

#
