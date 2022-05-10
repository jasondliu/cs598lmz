import bz2
# Test BZ2Decompressor and compress/decompress with bz2
decompressor = bz2.BZ2Decompressor()

uncompressed_data = decompressor.decompress(compressed_data)
print(uncompressed_data)

# bz2.compress() just calls compress() on a BZ2Compressor object
compressed_data = bz2.compress(original_data)
print(compressed_data)

uncompressed_data = bz2.decompress(compressed_data)
print(uncompressed_data)

# Encoding/Decoding
original_data = 'This is the original text.'

print('Original     :', repr(original_data))

encoded_data = original_data.encode('utf-8')
print('Encoded      :', repr(encoded_data))

decoded_data = encoded_data.decode('utf-8')
print('Decoded      :', repr(decoded_data))

# Unicode Errors
original_data = 'This is the original text.'

print('Original     :
