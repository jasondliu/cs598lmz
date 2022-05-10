import bz2
# Test BZ2Decompressor on a few files.

tfile = tempfile.TemporaryFile()

tfile.write(b'BZh91AY&SY\x80\x80\x00\x00\x00\x81\x00!\x9ah3M\x00 \x00!\x01\x80 \x08\x02\xe1\x02')
tfile.seek(0)
bz2file = bz2.BZ2File(tfile)
assert bz2file.read(100) == b'BZh91AY&SY\x80\x80\x00\x00\x00\x81\x00!\x9ah3M\x00 \x00!\x01\x80 \x08\x02\xe1\x02'
tfile.close()

tfile = tempfile.NamedTemporaryFile()
assert bz2.compress(b'hello world') == b'BZh91AY&SY\xe4\x00\x00\x1a\x00\x03\x00\x
