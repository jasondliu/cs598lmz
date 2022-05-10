import bz2
# Test BZ2Decompressor

bz2_data = b'this is some text'
compressed_data = bz2.compress(bz2_data)
len(compressed_data)

decompressor = bz2.BZ2Decompressor()

decompressor.decompress(compressed_data)

decompressor.unused_data

decompressor.decompress(b'and this is some more text') + decompressor.flush()

# The following will not work since the flush() method has already been called on the decompressor
#decompressor.decompress(b'and this is some more text')

#-------------------------------------------------------------------------------

import bz2

bz2_data = b'this is some text'
compressed_data = bz2.compress(bz2_data)

decompressor = bz2.BZ2Decompressor()
decompressed = decompressor.decompress(compressed_data)

print(decompressed)

#-------------------------------------------------------------------------------

import bz2

bz2_data = b
