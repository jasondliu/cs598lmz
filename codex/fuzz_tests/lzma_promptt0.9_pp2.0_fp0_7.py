import lzma
# Test LZMADecompressor with non-LZMA stream
data = BytesIO(b'this is not an LZMA compressed stream')
for d in [lzma.LZMADecompressor(), lzma.LZMADecompressor(format=lzma.FORMAT_XZ)]:
    with self.assertRaises(lzma.LZMAError) as cm:
        d.decompress(data.read())
    self.assertEqual(str(cm.exception),
        'Error -3 while decompressing: invalid distance code')
    self.assertEqual(d.unused_data, b'')
with self.assertRaises(lzma.LZMAError) as cm:
    lzma.decompress(b'this is not an LZMA compressed stream')
self.assertEqual(str(cm.exception),
    'Error -3 while decompressing: invalid distance code')
# Test LZMADecompressor with truncated stream
compressed = lzma.compress(b'one')
for d in [lzma.
