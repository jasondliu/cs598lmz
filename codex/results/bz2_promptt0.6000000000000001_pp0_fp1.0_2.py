import bz2
# Test BZ2Decompressor with a large input size.
# https://bugs.python.org/issue33001

data = b'\x42\x5a\x68\x39\x31\x41\x59\x26\x53\x59' * 10**7

with bz2.BZ2Decompressor() as dec:
    dec.decompress(data)
