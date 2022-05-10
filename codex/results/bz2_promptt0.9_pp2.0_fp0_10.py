import bz2
# Test BZ2Decompressor
f = bz2.open(__file__)
x = f.read()
f.close()
assert(x == open(__file__).read())

# Test BZ2File
f = bz2.BZ2File(__file__)
x = f.read()
f.close()
assert(x == open(__file__).read())

print 'OK'
