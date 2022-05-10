import bz2
# Test BZ2Decompressor

compressor = bz2.BZ2Compressor()
decompressor = bz2.BZ2Decompressor()

try:
    data = compressor.compress(b'The same line, over and over.\n')
    data += compressor.flush()
    print('Compressed:', len(data), 'bytes.')

    print(decompressor.decompress(data))
    print(decompressor.decompress(b'And a bit more data.'))
    print(decompressor.flush())
except IOError as e:
    print('Cannot decompress data:', e)
 

with bz2.BZ2File('lorem.txt.bz2', 'wb') as output:
    with open('lorem.txt', 'rb') as input:
        output.write(input.read())

with bz2.BZ2File('lorem.txt.bz2', 'rb') as input:
    print(input.readline())
    print(input.tell())
    print(input.seek(10))

