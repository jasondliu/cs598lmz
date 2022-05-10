import lzma
# Test LZMADecompressor
try:
    lzma.LZMACompressor()
except lzma.LZMAError as e:
    if e.errno == lzma.LZMA_UNSUPPORTED_CHECK:
        print "LZMA compression not supported"
    elif e.errno == lzma.LZMA_MEM_ERROR:
        print "Memory allocation failed"
    else:
        print "LZMA initialization failed:", e

compressor = lzma.LZMACompressor()
decompressor = lzma.LZMADecompressor()

data = b"a" * 100000
compressed = compressor.compress(data)
compressed += compressor.flush()
decompressed = decompressor.decompress(compressed)

print data == decompressed

# Test LZMAStream
try:
    lzma.LZMAStream()
except lzma.LZMAError as e:
    if e.errno == lzma.LZMA_UNSUPPORTED_CHECK:
        print "LZ
