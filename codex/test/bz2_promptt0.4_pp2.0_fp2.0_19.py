import bz2
# Test BZ2Decompressor

# Test BZ2Decompressor.__init__
try:
    bz2.BZ2Decompressor()
except Exception as e:
    print(e)

# Test BZ2Decompressor.decompress
try:
    bz2.BZ2Decompressor().decompress(b'BZh91AY&SY')
except Exception as e:
    print(e)

# Test BZ2Decompressor.decompress
try:
    bz2.BZ2Decompressor().decompress(b'BZh91AY&SY', 1)
except Exception as e:
    print(e)

# Test BZ2Decompressor.flush
try:
    bz2.BZ2Decompressor().flush()
except Exception as e:
    print(e)

# Test BZ2Decompressor.unused_data
try:
    bz2.BZ2Decompressor().unused_data
except Exception as e:
    print(e)

# Test BZ2Decompressor.
