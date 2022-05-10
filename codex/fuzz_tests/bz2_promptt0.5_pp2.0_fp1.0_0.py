import bz2
# Test BZ2Decompressor.
bz2dec = bz2.BZ2Decompressor()
bz2dec.decompress(bz2data)

# Test BZ2File.
bz2file = bz2.BZ2File('test.bz2', 'rb')
bz2file.read()
bz2file.seek(0)
bz2file.read()
bz2file.close()

# Test BZ2File with a filename.
bz2file = bz2.BZ2File('test.bz2', 'rb')
bz2file.read()
bz2file.close()

# Test BZ2File with a file object.
fileobj = open('test.bz2', 'rb')
bz2file = bz2.BZ2File(fileobj)
bz2file.read()
bz2file.close()
fileobj.close()

# Test BZ2File with a file object and a filename.
fileobj = open('test.bz2', 'rb')
bz2file
