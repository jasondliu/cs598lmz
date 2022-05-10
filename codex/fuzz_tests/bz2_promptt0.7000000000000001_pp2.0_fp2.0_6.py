import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SY.P@\xc9\x14\xe1"\x06\xa0\x1b\x88\x00\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00!\x9ah3M\x13<]\xc9\x14\xe1\x02\x00'
d = bz2.BZ2Decompressor()
d.decompress(data)
d.flush()

# Test BZ2File
bz2file = bz2.BZ2File('test.bz2', 'rb')
bz2file.seek(5)
bz2file.read()
bz2file.seek(5)
bz2file.read(3)
bz2file.tell()
# Test BZ2File with a non file-like object
t = BytesIO(b'123
