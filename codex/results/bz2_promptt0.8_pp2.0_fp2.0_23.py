import bz2
# Test BZ2Decompressor =============
print("===TEST BZ2 DECOMPRESSOR===")
compressor = bz2.BZ2Decompressor()
with open('PHL_housing_prices.csv.bz2', 'rb') as data:
    decompressed = b''
    for block in iter(lambda: data.read(100 * 1024), b''):
        decompressed += compressor.decompress(block)
print(decompressed[:100], b'\n')

# Test BZ2Compressor =============
print("===TEST BZ2 COMPRESSOR===")
compressor = bz2.BZ2Compressor()
with open('PHL_housing_prices.csv', 'rb') as data:
    compressed = b''
    for block in iter(lambda: data.read(100 * 1024), b''):
        compressed += compressor.compress(block)
    compressed += compressor.flush()
print(compressed[:100], b'\n')
with open('PHL_housing_prices.csv.bz2', 'wb') as f:

