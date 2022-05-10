import bz2
# Test BZ2Decompressor

data = bz2.compress(bytes('This is a string', 'utf-8'))

decompressor = bz2.BZ2Decompressor()

try:
    print(decompressor.decompress(data))
except EOFError:
    print('Not enough data to decompress')

