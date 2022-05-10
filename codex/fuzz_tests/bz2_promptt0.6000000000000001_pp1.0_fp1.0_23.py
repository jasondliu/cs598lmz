import bz2
# Test BZ2Decompressor

# Reusable compressor and decompressor objects
c = bz2.BZ2Compressor()
d = bz2.BZ2Decompressor()

original_data = b'This is the original text.'
print('Original     :', len(original_data), original_data)

compressed = c.compress(original_data)
compressed += c.flush()
print('Compressed   :', len(compressed), compressed)

decompressed = d.decompress(compressed)
print('Decompressed :', len(decompressed), decompressed)

# Test BZ2File

bz2_compressor = bz2.BZ2Compressor()
data = b'This is the original text.'
with open('example.bz2', 'wb') as output:
    output.write(bz2_compressor.compress(data))
    output.write(bz2_compressor.flush())

with bz2.BZ2File('example.bz2', 'rb') as input:
    print(input.read())
