import bz2
# Test BZ2Decompressor.partial
tmpfile = os.path.join(support.TESTFN, "tmp")
f = bz2.BZ2File(bz2.BZ2File.name, "rb")
dec = bz2.BZ2Decompressor()
with open(tmpfile, "wb") as tmp:
    for chunk in iter(lambda : f.read(100000), b""):
        tmp.write(dec.decompress(chunk))
    tmp.write(dec.flush())
with open(bz2.BZ2File.name, "rb") as reference:
    with open(tmpfile, "rb") as reconstituted:
        self.assertEqual(reconstituted.read(), reference.read())
os.remove(tmpfile)
# Test BZ2Compressor.partial
bz2.BZ2Compressor()
# Without an argument
comp = bz2.BZ2Compressor()
data = comp.compress(TEXT)
data += comp.flush()
self.assertEqual(bz2.decompress(data),
