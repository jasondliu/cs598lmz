import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

try:
    original_data = decompressor.decompress(compressed_data)

except EOFError:
    print('Compressed contents were truncated.')

else:
    print('Decompressed length:', len(original_data))
    print(original_data)

# Decompress

compressed_data = bz2.compress(original_data)

print('Compressed length:', len(compressed_data))
print(compressed_data)

# Compress

original_data = b'This is the original text.'

print('Original:', len(original_data), original_data)
import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

try:
    original_data = decompressor.decompress(compressed_data)

except EOFError:
    print('Compressed contents were truncated.')

else:
    print('Decompressed length:',
