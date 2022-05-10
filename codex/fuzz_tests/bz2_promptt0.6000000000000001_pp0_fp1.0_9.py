import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
file = bz2.BZ2File('/Users/tongwang/Downloads/enwiki-latest-pages-articles.xml.bz2')
for i in range(0,10):
    data = file.read(100*1024)
    if not data:
        break
    print decompressor.decompress(data)
file.close()

# Test BZ2File
file = bz2.BZ2File('/Users/tongwang/Downloads/enwiki-latest-pages-articles.xml.bz2')
for i in range(0,10):
    data = file.read(100*1024)
    if not data:
        break
    print data
file.close()
