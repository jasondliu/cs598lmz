import bz2
# Test BZ2Decompressor

with open('data/lorem.txt.bz2', 'rb') as input:
    decompressor = bz2.BZ2Decompressor()
    with open('data/lorem_copy.txt', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(block))
        output.write(decompressor.flush())

with open('data/lorem.txt') as input, open('data/lorem_copy.txt') as output:
    print(input.read() == output.read())

import bz2

original_data = b'This is the original text.'
print('Original     :', len(original_data), original_data)

compressed = bz2.compress(original_data)
print('Compressed   :', len(compressed), compressed)

decompressed = bz2.decompress(compressed)
print('Decompressed :', len(decompressed), decompressed)

print(original_
