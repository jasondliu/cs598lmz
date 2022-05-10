import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

try:
    with open('sample.bz2', 'rb') as input, \
         open('uncompressed.txt', 'wb') as output:
        while True:
            block = input.read(100)
            if not block:
                break
            uncompressed = decompressor.decompress(block)
            if uncompressed:
                output.write(uncompressed)
            else:
                print('No uncompressed data')
except EOFError:
    print('Not a bzip2 file')

# Test BZ2File

with bz2.BZ2File('sample.bz2') as input:
    print('Entire file:', input.read())

with bz2.BZ2File('sample.bz2') as input:
    for line in input:
        print(line)

with bz2.BZ2File('sample.bz2') as input:
    print('First line:', input.readline())
    print('Second line:
