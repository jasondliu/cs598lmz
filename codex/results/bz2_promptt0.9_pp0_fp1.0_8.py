import bz2
# Test BZ2Decompressor and BZ2Compressor with a three-byte payload
payload = b'abc'

compressor = bz2.BZ2Compressor()
compressed = compressor.compress(payload)
compressed += compressor.flush()
compressed_size = len(compressed)
# Returns bytes object:
compressed

# Will create an empty payload if passed bytes-like object:
decompressor = bz2.BZ2Decompressor()
decompressed = decompressor.decompress(compressed)
decompressed += decompressor.flush()
decompressed

print('Original length:          %d' % len(payload))
print('Compressed length:        %d' % len(compressed))
print('Decompressed length:      %d' % decompressed_size)
print('Decompressed payload:     %s' % decompressed)

print('\nOriginal payload:         %s' % payload)
print('Converted payload:        %s' % decompressed)

print('Does converted payload    %s original?' % (
    'match' if payload ==
