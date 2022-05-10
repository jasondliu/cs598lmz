import bz2
# Test BZ2Decompressor read into memory
with open('enwiki-latest-pages-articles.xml.bz2', 'rb') as zf:
    z = bz2.BZ2Decompressor()
    orig = open('enwiki-latest-pages-articles.xml', 'rb').read()[:10000]
    content = z.decompress(zf.read(10000))
    print(content == orig)

# Same as above for gzip
with open('enwiki-latest-pages-articles.xml.gz', 'rb') as gzf:
    gz = gzip.GzipFile(fileobj=gzf)
    orig = open('enwiki-latest-pages-articles.xml', 'rb').read()[:10000]
    content = gz.read(10000)
    print(content == orig)

# Both of Xzip.bz2/gz are identical to original file
print(xzip.gzip.read(7000) == xzip.bzip2.read(7000))

# As of 11.7, Xzip.gzip = Xzip.b
