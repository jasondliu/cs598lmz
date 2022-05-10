import bz2
# Test BZ2Decompressor with an extra byte
decompressor = bz2.BZ2Decompressor()
try:
    data = decompressor.decompress(b'BZh91')
except OSError as err:
    print(err)

# Test BZ2Decompressor with a truncated member
decompressor = bz2.BZ2Decompressor()
try:
    data = decompressor.decompress(b'BZh91')
except OSError as err:
    print(err)

# Test BZ2Decompressor with a truncated member and extra data
decompressor = bz2.BZ2Decompressor()
try:
    data = decompressor.decompress(b'BZh91A')
except OSError as err:
    print(err)
