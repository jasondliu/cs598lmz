import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()

for chunk in iter(lambda: file.read(100 * 1024), b''):
    decompressed = decompressor.decompress(chunk)
    if decompressed:
        print(decompressed)

remainder = decompressor.unused_data
print(remainder)

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()

for data in ['aaa', 'bbb', 'ccc', 'ddd']:
    compressed = compressor.compress(data)
    print(compressed)

remainder = compressor.flush()
print(remainder)

# Test BZ2File
with bz2.BZ2File('file.bz2', 'wb') as output:
    output.write(b'abc')
    output.write(b'def')

with bz2.BZ2File('file.bz2', 'rb') as input:
    print(input.read(2))
    print(input.read
