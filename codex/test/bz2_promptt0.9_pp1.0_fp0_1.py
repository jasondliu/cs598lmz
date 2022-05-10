import bz2
# Test BZ2Decompressor to see what is the maximal amount of bytes
# it can consume.
max_consume = 1
for (i, c) in enumerate([b'a', b'b', b'c', b'd', b'e', b'f', b'g']):
    data = [b'x', b'x', b'x', b'x', b'x', b'x', b'x', b'x', b'x', b'x', b'x',
            b'x', b'x', b'x', b'x', b'x', b'x', b'x', b'x', b'x', b'x', b'x',
            b'x', b'x', b'x', b'x', b'x', b'x', b'x', c]
    d = bz2.BZ2Decompressor()
