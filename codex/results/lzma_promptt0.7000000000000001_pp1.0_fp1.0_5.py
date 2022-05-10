import lzma
# Test LZMADecompressor(format=FORMAT_ALONE)

x = lzma.LZMADecompressor()

# Decompress the default-compressed test string

x.decompress(TEST1_XZ)

# Decompress the raw-encoded test string

x.decompress(TEST1_RAW)

# Decompress the xz-encoded test string

x.decompress(TEST1_XZ)

# Decompress the auto-encoded test string

x.decompress(TEST1_AUTO)

# Decompress a raw-encoded string with an incorrect check

try:
    x.decompress(TEST2_RAW)
except lzma.LZMAError:
    pass
else:
    print('TEST2_RAW did not raise LZMAError')

# Decompress an xz-encoded string with an incorrect check

try:
    x.decompress(TEST2_XZ)
except lzma.LZMAError:
    pass

