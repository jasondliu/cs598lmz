import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

data = open('sample.bz2', 'rb').read()

decompressed = decompressor.decompress(data)

open('sample.out', 'wb').write(decompressed)
# Test BZ2File

import bz2

bz_file = bz2.BZ2File('sample.bz2')

content = bz_file.read()

open('sample.out', 'wb').write(content)
# Test BZ2Compressor

import bz2

compressor = bz2.BZ2Compressor()

content = open('sample.txt', 'rb').read()

compressed = compressor.compress(content)
compressed += compressor.flush()

open('sample.bz2', 'wb').write(compressed)
# Test BZ2File

import bz2

bz_file = bz2.BZ2File('sample.bz2', 'wb')

bz_file.write(
