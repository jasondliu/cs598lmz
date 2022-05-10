import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed)

# BZ2File
with bz2.BZ2File('example.bz2', 'wb') as output:
    for line in lines:
        output.write(line)

with bz2.BZ2File('example.bz2', 'rb') as input:
    for line in input:
        print(line)

# compress data incrementally
compressor = bz2.BZ2Compressor()
data = b'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

compressor.compress(data)
compressor.flush()

# compress data non-incrementally
compressed = bz2.compress(data)
decompressed = bz2.decompress(compressed)

# compress a file non-incrementally
with open('/etc/hosts', 'rb') as input:
    data = input.read()

with bz2.BZ2File('/tmp/example.bz
