from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

print('\n --- PYTHON CODE --- \n')
print('Compressing with pybrotli...')
data = get_binaries()
data = brotli.compress(data)
print(data)
