import bz2
# Test BZ2Decompressor by decompressing a file.
decompressor = bz2.BZ2Decompressor()
file = open('sample.bz2', 'rb')
while True:
    block = file.read(100000)
    if not block:
        break
    uncompressed = decompressor.decompress(block)
    if uncompressed:
        print(uncompressed)
    else:
        print('.', end=' ')
# Show that the decompressor has finished decompressing the file.
print(decompressor.decompress(b''))
# Show that the decompressor can no longer decompress any more data.
print(decompressor.decompress(b'blahblah'))

###############################################################################
#
#    Copyright (C) 2015 by
#    @author: Emmanuel Nataf <emmanuel.nataf@gmail.com>
#    All rights reserved.
#    BSD license.
#
# Authors:
#   Emmanuel Nataf (May 2015)
#
#
import bz2
# Test BZ2Compressor by compressing
