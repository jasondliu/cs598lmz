import lzma
# Test LZMADecompressor directly.
d = lzma.LZMADecompressor()
data = b'\x00\x00\x00\x01\x00!\x9c\xdbW\x01\xc0\xaf,!\x00\x00\x00\x04'
d.decompress(data)
d.unused_data
d.decompress(b'\x00\x00\x00\x04')
d.decompress(b'ing.')
# Test with context manager.
with lzma.open(TESTFN, 'rb') as f:
    data = f.read()
    f.close()
    f.closed
    with self.assertRaises(ValueError):
        f.read()
with lzma.open(TESTFN, mode='r') as f:
    with self.assertRaises(TypeError):
        f.write(b'')
    with self.assertRaises(TypeError):
        f.fileno()
    with self.assertRaises((AttributeError, io.Un
