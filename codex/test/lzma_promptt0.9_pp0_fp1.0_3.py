import lzma
# Test LZMADecompressor on some input data.  Multiple LZMADecompressor()
# objects reuse the same internal per-stream state.  This allows processes
# to work in parallel with one lzma.LZMADecompressor() object per process.

n = 100
i = 1
print ("Starting...")
