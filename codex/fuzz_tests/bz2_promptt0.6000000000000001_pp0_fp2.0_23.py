import bz2
# Test BZ2Decompressor
#
# This example shows how to read data from a BZ2 file.

# Read compressed data
with bz2.BZ2File('lorem.txt.bz2', 'rb') as input:
    print('Entire file:')
    all_data = input.read()
    print(all_data)

# Read line by line
print('Line by line:')
with bz2.BZ2File('lorem.txt.bz2', 'rb') as input:
    for line in input:
        print(line)

# Read using a decompressor
decompressor = bz2.BZ2Decompressor()
with open('lorem.txt.bz2', 'rb') as input:
    while True:
        block = input.read(1024)
        if not block:
            break
        print(decompressor.decompress(block))

# Read using a decompressor with multiple concatenated streams
decompressor = bz2.BZ2Decompressor()
with open('python.tar.bz2', 'rb
