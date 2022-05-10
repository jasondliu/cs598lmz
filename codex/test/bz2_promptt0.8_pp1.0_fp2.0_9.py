import bz2
# Test BZ2Decompressor
# NOTE - this is a partial test
# Test BZ2FileDecompressor
# Test BZ2FileCompressor
# Test BZ2File
def _test():
    import doctest, test_bz2
    return doctest.testmod(test_bz2)


