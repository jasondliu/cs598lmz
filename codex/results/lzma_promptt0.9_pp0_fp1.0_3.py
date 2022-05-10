import lzma
# Test LZMADecompressor on some input data.  Multiple LZMADecompressor()
# objects reuse the same internal per-stream state.  This allows processes
# to work in parallel with one lzma.LZMADecompressor() object per process.

n = 100
i = 1
print ("Starting...")
for i in range (1,6):
    foo2 = open('lzma%s.txt' % i, 'r')
    foo2c = foo2.read()
    foo2.close()

    lzc = lzma.LZMADecompressor()
    print ("Opening %s" % i)
# Note that the output of a LZMA stream varies in size.
    data = lzc.decompress(foo2c)
    print ("Result: %s bytes" % len(data))
    print ("Testing...")
    for n in range(len(data)):
        try:
            assert data[n] == (n & 255)
        except AssertionError:
            print(n, data[n])
# Process some more data.
