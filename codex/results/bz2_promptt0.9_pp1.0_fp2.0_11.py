import bz2
# Test BZ2Decompressor with partial feeds and a get_read_size equal to the
# file size.
comp = bz2.BZ2Decompressor()
d = comp.decompress(bz2data[:1])
self.assertEqual(d, "")
d = comp.decompress(bz2data[1:1024])
self.assertEqual(d, "")
d = comp.decompress(bz2data[1024:len(bz2data)])
self.assertEqual(d, plaintext)
# Test BZ2Decompressor with chunks and decompressobj.
d = ""
for i in range(0, len(bz2data), 1024):
    d += comp.decompress(bz2data[i:i+1024])
self.assertEqual(d, plaintext)
# Test BZ2Decompressor against all file at once.
comp = bz2.BZ2Decompressor()
d = comp.decompress(bz2data)
self.assertEqual(d, plaintext)
# Test BZ2
