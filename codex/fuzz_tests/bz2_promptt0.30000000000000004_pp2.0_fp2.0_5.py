import bz2
# Test BZ2Decompressor

bz2_decompressor = bz2.BZ2Decompressor()

with open('data/enwiki-latest-pages-articles.xml.bz2', 'rb') as input:
    with open('data/enwiki-latest-pages-articles.xml', 'wb') as output:
        while True:
            block = input.read(1024)
            if not block:
                break
            output.write(bz2_decompressor.decompress(block))
 
# Test BZ2File

with bz2.BZ2File('data/enwiki-latest-pages-articles.xml.bz2', 'rb') as input:
    with open('data/enwiki-latest-pages-articles.xml', 'wb') as output:
        while True:
            block = input.read(1024)
            if not block:
                break
            output.write(block)
 
# Test BZ2File with context manager

with bz2.BZ2File('data/enwiki-latest-pages-articles.xml.bz
