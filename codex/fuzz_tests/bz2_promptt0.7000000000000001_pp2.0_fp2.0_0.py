import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
compr = bz2.compress(b'hello')
compr += b'a' * (1024 - len(compr))
print(decompressor.decompress(compr))
print(decompressor.decompress(compr))
print(decompressor.decompress(b'hello'))

print(decompressor.unconsumed_tail)
print(decompressor.eof)

# Test BZ2File
testfname = support.TESTFN
testfpath = os.path.join(support.TEMPDIR, testfname)

def create_file(filename, data):
    f = open(filename, "wb")
    f.write(data)
    f.close()

def read_file(filename):
    f = open(filename, "rb")
    data = f.read()
    f.close()
    return data

def test_one(filename, mode, testdata):
    created = 0
    try:
        os
