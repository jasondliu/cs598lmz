import bz2
# Test BZ2Decompressor
d = bz2.BZ2Decompressor()
d.decompress(open('/Users/carson/Downloads/enwiki-latest-pages-articles.xml.bz2').read())
