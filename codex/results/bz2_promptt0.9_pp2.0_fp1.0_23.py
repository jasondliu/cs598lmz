import bz2
# Test BZ2Decompressor / Compressor pair
#
# Todo:
# - share compression objects (with different compression level)?
#   (see also bz2.BZ2Compressor.copy)
# - test use of BZ2File
# - test other options with BZ2File
# - test incremental compression / decompression
# - compression objects with initargs

if support.verbose:
    print('\nTesting BZ2Compressor/BZ2Decompressor objects')

# string buffers

for s, m in [("123", 1),
             ("12"*1000, 300),
             (10000*"123456xyz", 3333),
             (20000*"123456xyzA", 3333),
             ]:
    for level in [-1, 0, 1, 9]:
        for wbits in [-15, 15]:
            for bufsize in [0, 1, 2, 5, 8, 15, 16, 17,
                            200, 1000, 10000, s, 10000]:
                if support.verbose:
                    print('   %r level %s, wbits %d, buf
