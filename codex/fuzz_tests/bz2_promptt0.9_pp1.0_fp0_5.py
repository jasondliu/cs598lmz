import bz2
# Test BZ2Decompressor.decompress() that returns less than
# the requested amount
co = bz2.BZ2Compressor(9)
t = co.compress(b'x' * 1000)
co.flush(bz2.FINISH)
t += co.flush()
d = bz2.BZ2Decompressor()
d.decompress(t[:1000])

try:
    d.decompress(t[1000:], 500)
except EOFError:
    pass
else:
    raise RuntimeError("didn't raise EOFError")

try:
    d.decompress(t[1000:], 1000)
    raise RuntimeError("didn't raise EOFError")
except EOFError as e:
    if str(e) != 'incomplete data stream':
        raise
# Test empty input to BZ2Decompressor.decompress()
co = bz2.BZ2Compressor()
t = co.compress(b'x' * 1000)
co.flush(bz2.FINISH)
t += co.flush()
d
