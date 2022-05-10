import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('python.bz2', 'rb') as input:
    with open('python.txt', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(block))

print('Decompressed')

# Test BZ2File

bz_file = bz2.BZ2File('python.bz2')
data = bz_file.read()
print(data.decode('utf-8'))
bz_file.close()

# Test BZ2Compressor

compressor = bz2.BZ2Compressor(9)

with open('python.bz2', 'wb') as output:
    with open('python.txt', 'rb') as input:
        while True:
            block = input.read(1024)
            if not block:
                break
            output.write(compressor.compress(block))
        output.write(
