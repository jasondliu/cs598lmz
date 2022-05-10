import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

decompressed_data = decompressor.decompress(compressed_data)

print('Decompressed is {} bytes'.format(len(decompressed_data)))

original_data = open('lorem.txt', 'rb').read()

print('Original is {} bytes'.format(len(original_data)))

print(decompressed_data == original_data)

# Test BZ2File

with bz2.BZ2File('lorem.txt.bz2', 'rb') as input:
    print(len(input.read()))

with bz2.BZ2File('lorem.txt.bz2', 'rb') as input:
    for line in input:
        print(line)

# Compress data using BZ2File

with bz2.BZ2File('lorem.txt.bz2', 'wb') as output:
    with open('lorem.txt', 'rb') as input:
        output.write(input.read
