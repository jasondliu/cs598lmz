import bz2
# Test BZ2Decompressor class.

import bz2
from test import support

def check_bz2(data):
    compressor = bz2.BZ2Compressor()
    uncompress = bz2.BZ2Decompressor().decompress
    for func in (compressor.compress, compressor.flush):
        compressed = func(data)
        if compressed:
            uncompressed = uncompress(compressed)
            if uncompressed != data:
                raise AssertionError(
                    'bug in BZ2 compressor/decompressor (data %r)' % data)

def check_buffers(data):
    compressor = bz2.BZ2Compressor()
    uncompress = bz2.BZ2Decompressor().decompress

    for func in (compressor.compress, compressor.flush):
        buffer = bytearray()
        func(data, buffer)
        compressed = bytes(buffer)
        if compressed:
            buffer = bytearray()
            uncompress(compressed, buffer)
            uncompressed = bytes(buffer)
            if uncompressed
