import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()
with open('/Users/j35/Desktop/test.txt.bz2', 'rb') as f:
    file_content = f.read()
    # print(file_content)
    print(decompressor.decompress(file_content))

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()
uncompressed_data = b'Hello World'
compressed_data = compressor.compress(uncompressed_data)
print(compressed_data)

# Test BZ2File

with bz2.BZ2File('/Users/j35/Desktop/test.txt.bz2', 'rb') as input:
    print(input.read())
    for line in input:
        print(line)

with bz2.BZ2File('/Users/j35/Desktop/test.txt.bz2', 'wb') as output:
    output.write(b'Hello World')

with bz2.BZ
