import bz2
# Test BZ2Decompressor

compressor = bz2.BZ2Compressor()
decompressor = bz2.BZ2Decompressor()

compressed = compressor.compress(b"this is a test")
compressed += compressor.flush()

decompressed = decompressor.decompress(compressed)
print(decompressed)

decompressor = bz2.BZ2Decompressor()

try:
    data = decompressor.decompress(b"some invalid compressed data")
except OSError as err:
    print('Cannot decompress data:', err)

decompressor = bz2.BZ2Decompressor()

try:
    data = decompressor.decompress(b"BZh91AY&SY")
except OSError as err:
    print('Cannot decompress data:', err)

decompressor = bz2.BZ2Decompressor()

try:
    data = decompressor.decompress(b"BZh91AY&SY\xaf\x82\r\x00
