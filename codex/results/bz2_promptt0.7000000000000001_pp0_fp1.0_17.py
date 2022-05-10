import bz2
# Test BZ2Decompressor.
decomp = bz2.BZ2Decompressor()
decomp.decompress(compressed)

# Test BZ2File.
bz_in = bz2.BZ2File('sample.bin', 'rb')
bz_out = bz2.BZ2File('sample.bz2', 'wb')

bz_out.write('This is a test')
bz_out.flush()

print bz_in.read()
bz_out.close()
bz_in.close()

print '-' * 50

import gzip
# Test GzipFile.
gz_in = gzip.GzipFile('sample.gz', 'rb')
gz_out = gzip.GzipFile('sample.gz', 'wb')

gz_out.write('This is a test')
gz_out.flush()

print gz_in.read()
gz_out.close()
gz_in.close()

print '-' * 50

import zlib
# Test zlib.
data = 'This is a
