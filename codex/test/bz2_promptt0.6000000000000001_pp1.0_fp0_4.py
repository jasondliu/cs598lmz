import bz2
# Test BZ2Decompressor
try:
    bz2.BZ2Decompressor()
    print('BZ2 support is available')
except:
    print('BZ2 support is not available')
    
# Test LZMA
try:
    import lzma
    print('LZMA support is available')
except:
    print('LZMA support is not available')

# Test LZ4
try:
    import lz4
    print('LZ4 support is available')
except:
    print('LZ4 support is not available')
    
# Test Snappy
try:
    import snappy
    print('Snappy support is available')
except:
    print('Snappy support is not available')

# Test Brotli
try:
    import brotli
    print('Brotli support is available')
except:
    print('Brotli support is not available')

# Test Zstd
try:
    import zstandard as zstd
    print('Zstd support is available')
except:
    print('Zstd support is not available')

# Test Zlib

