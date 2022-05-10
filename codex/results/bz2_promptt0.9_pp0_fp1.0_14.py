import bz2
# Test BZ2Decompressor on empty data.
bz2.decompress(b'') is b''

# Test compress_output with small input.
bz2.decompress(b'BZ') is None

# Test Decompressor on bad input.
for wrong_starting_char in b'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#%&()*+,-./:;<=>?@[]^_{|}~':
    bz2.decompress(wrong_starting_char)

# Test decompress_unused_data with bad input.
for wrong_starting_char in b'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#%&()*+,-./:;<=>?@[]^_{|}~':
    bz2.decompress_unused_data(wrong_starting_char)

# Test both decompress() and decompress_unused_
