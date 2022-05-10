import lzma
# Test LZMADecompressor
c = lzma.LZMADecompressor()
with open("/home/paul/Downloads/enwiki-latest-pages-articles.xml.bz2", "rb") as f:
    data = f.read(1024)
    while data:
        print(c.decompress(data))
        data = f.read(1024)

# Test LZMAFile
with lzma.open("/home/paul/Downloads/enwiki-latest-pages-articles.xml.bz2") as f:
    for line in f:
        print(line)

# Test LZMACompressor
c = lzma.LZMACompressor()
with open("/home/paul/Downloads/enwiki-latest-pages-articles.xml.bz2", "rb") as f:
    data = f.read(1024)
    while data:
        print(c.compress(data))
        data = f.read(1024)

# Test LZMAFile
with lzma.open("/home/paul/
