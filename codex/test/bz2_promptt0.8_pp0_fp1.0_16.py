import bz2
# Test BZ2Decompressor
bz2c = bz2.BZ2Decompressor()

#Test bz2 decompression
bz2c.decompress(b'\x42\x5a\x68\x39\x31\x41\x59\x26\x53\x59')

#Test bz2 decompression after initial bytes
