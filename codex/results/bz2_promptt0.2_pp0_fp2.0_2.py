import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/enwiki-latest-pages-articles.xml.bz2', 'rb') as input:
    with open('data/enwiki-latest-pages-articles.xml', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(block))

# Test BZ2File

with bz2.BZ2File('data/enwiki-latest-pages-articles.xml.bz2', 'rb') as input:
    with open('data/enwiki-latest-pages-articles.xml', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(block)

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('data/enwiki-latest-pages-articles.xml', 'rb') as input:
    with open('data/en
