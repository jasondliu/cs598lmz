import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

try:
    with open('lorem.txt.bz2', 'rb') as input:
        with open('lorem_copy.txt', 'wb') as output:
            while True:
                block = input.read(1024)
                if not block:
                    break
                output.write(decompressor.decompress(block))
except IOError as err:
    print('Error opening files:', str(err))

print('Decompressed!')

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

