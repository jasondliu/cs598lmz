import bz2
# Test BZ2Decompressor

d = bz2.BZ2Decompressor()
f = open('bz2decompressor.py', 'rb')
b = f.read(100)
while b:
    data = d.decompress(b)
    print data,
    b = f.read(100)
print d.decompress(b)
