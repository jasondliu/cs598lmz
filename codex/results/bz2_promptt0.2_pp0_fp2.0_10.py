import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/enwiki-latest-pages-articles.xml.bz2', 'rb') as input:
    with open('data/enwiki-latest-pages-articles.xml', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(block))
 
# Test BZ2File

with bz2.BZ2File('data/enwiki-latest-pages-articles.xml.bz2', 'rb') as input, \
     open('data/enwiki-latest-pages-articles.xml', 'wb') as output:
    for block in iter(lambda: input.read(100 * 1024), b''):
        output.write(block)
 
# Test BZ2File with context manager

with bz2.BZ2File('data/enwiki-latest-pages-articles.xml.bz2', 'rb') as input, \
     open('data/en
