import bz2
# Test BZ2Decompressor and BZ2Compressor objects
testdata = b'Please compress me'
testdata2 = b''
for i in range(1000):
    testdata2 += testdata
compressor = bz2.BZ2Compressor()
compressed = compressor.compress(testdata2) + compressor.flush()
decompressor = bz2.BZ2Decompressor()
decompressed = decompressor.decompress(compressed)
# Test BZ2File
with bz2.BZ2File('/tmp/tmp.bz2', 'w') as f:
    f.write(testdata2)
with bz2.BZ2File('/tmp/tmp.bz2', 'r') as f:
    for line in f:
        print(line)

import bz2
# Test BZ2File with compresslevel
with bz2.BZ2File('/tmp/tmp.bz2', 'w', compresslevel=9) as f:
    f.write(testdata2)
with bz2.BZ2File('/tmp/
