import bz2
# Test BZ2Decompressor -- a lot of data to decompress, and some random
# seeks, but the data is short enough that we can just save it in memory
# and compare it to the reference output
decomp = bz2.BZ2Decompressor()
compr = bz2.compress(open(bz2.__file__, 'rb').read())
decompdata = decomp.decompress(compr)
assert decompdata == open(bz2.__file__, 'rb').read()
