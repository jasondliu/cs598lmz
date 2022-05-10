import bz2
# Test BZ2Decompressor

bz2_decompressor = bz2.BZ2Decompressor()

with open('enwiki-latest-pages-articles.xml.bz2', 'rb') as f_in, open('enwiki-latest-pages-articles.xml', 'wb') as f_out:
    for block in iter(lambda: f_in.read(100 * 1024), b''):
        f_out.write(bz2_decompressor.decompress(block))
 
# Test BZ2File

with bz2.BZ2File('enwiki-latest-pages-articles.xml.bz2', 'rb') as f_in, open('enwiki-latest-pages-articles.xml', 'wb') as f_out:
    for block in iter(lambda: f_in.read(100 * 1024), b''):
        f_out.write(block)
 
# Test BZ2File with context manager

with bz2.BZ2File('enwiki-latest-pages-articles.xml.bz2', 'rb') as f_
