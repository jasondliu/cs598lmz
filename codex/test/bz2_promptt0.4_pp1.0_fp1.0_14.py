import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

try:
    with open('lorem.txt.bz2', 'rb') as input, open('lorem_copy.txt', 'wb') as output:
        while True:
            block = input.read(100)
            if not block:
                break
            output.write(decompressor.decompress(block))
except IOError as err:
    print('Error opening files:', str(err))

print('Decompressed')

# Test BZ2File

try:
    with bz2.BZ2File('lorem.txt.bz2', 'rb') as input, open('lorem_copy.txt', 'wb') as output:
        for data in iter(lambda: input.read(100), b''):
            output.write(data)
except IOError as err:
    print('Error opening files:', str(err))

print('Decompressed')

# Test BZ2File with context manager

