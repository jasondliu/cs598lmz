import bz2
# Test BZ2Decompressor
data = open("../data/enwiki-latest-pages-articles.xml.bz2", "rb").read(100)
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(data)

# Test BZ2File
bz2_file = bz2.BZ2File("../data/enwiki-latest-pages-articles.xml.bz2")
bz2_file.read(100)
bz2_file.close()

# Test BZ2Compressor
data = open("../data/enwiki-latest-pages-articles.xml", "rb").read(100)
compressor = bz2.BZ2Compressor()
compressor.compress(data)
compressor.flush()

# Test open
open("../data/enwiki-latest-pages-articles.xml.bz2", "rb")
open("../data/enwiki-latest-pages-articles.xml.bz2", "wb")
open("../data/enwiki-latest-pages-articles.xml.bz2
