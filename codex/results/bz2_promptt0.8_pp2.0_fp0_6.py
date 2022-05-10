import bz2
# Test BZ2Decompressor for multi-stream decompression (incomplete read)

# This is a test file created by:
#    bzcat /bin/ls | bzip2 --best > a.bz2
f = open('a.bz2', 'rb')
bz = bz2.BZ2Decompressor()
while True:
    data = f.read(100)
    if not data:
        break
    print(bz.decompress(data))
print(bz.flush())
f.close()
