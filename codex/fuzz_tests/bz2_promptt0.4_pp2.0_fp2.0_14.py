import bz2
# Test BZ2Decompressor
for i in range(10):
    with bz2.open('/Users/nathan/Downloads/enwiki-latest-pages-articles10.xml-p10p30302.bz2', 'rb') as f:
        print(f.read(100))

# Test BZ2Compressor
with open('/Users/nathan/Downloads/enwiki-latest-pages-articles10.xml-p10p30302.bz2', 'rb') as f:
    c = bz2.BZ2Compressor()
    print(c.compress(f.read(100)))
    print(c.flush())

# Test BZ2File
with bz2.BZ2File('/Users/nathan/Downloads/enwiki-latest-pages-articles10.xml-p10p30302.bz2', 'rb') as f:
    print(f.read(100))

with bz2.BZ2File('/Users/nathan/Downloads/enwiki-latest-pages-articles10.xml-p10p30302.
