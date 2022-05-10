import bz2
# Test BZ2Decompressor

bz2_decompressor = bz2.BZ2Decompressor()

with open('data/enwiki-latest-pages-articles.xml.bz2', 'rb') as f:
    file_content = f.read()
    decompressed_data = bz2_decompressor.decompress(file_content)
    
    with open('data/enwiki-latest-pages-articles.xml', 'wb') as f:
        f.write(decompressed_data)
 
# Test BZ2File

with bz2.BZ2File('data/enwiki-latest-pages-articles.xml.bz2', 'rb') as source, open('data/enwiki-latest-pages-articles.xml', 'wb') as dest:
    file_content = source.read()
    dest.write(file_content)
 
# Test BZ2File with context manager

with bz2.BZ2File('data/enwiki-latest-pages-articles.xml.bz2', 'rb') as source:
    file_
