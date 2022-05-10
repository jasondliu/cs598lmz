import bz2
# Test BZ2Decompressor

decompressor = BZ2Decompressor()

data = open('lorem.txt.bz2', 'rb').read()

decompressed_data = decompressor.decompress(data)

print(decompressed_data)

decompressor = bz2.BZ2Decompressor()

data = open('lorem.txt.bz2', 'rb').read()

decompressed_data = decompressor.decompress(data)

print(decompressed_data)

# Compress data

compressor = bz2.BZ2Compressor()

uncompressed_data = b'We are no longer the knights who say ni!'

compressed_data = compressor.compress(uncompressed_data)

print(compressed_data)

# Finish compression

compressor = bz2.BZ2Compressor()

uncompressed_data = b'We are no longer the knights who say ni!'

compressed_data = compressor.compress(uncompressed_data)

more_data =
