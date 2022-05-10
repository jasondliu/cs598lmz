import bz2
# Test BZ2Decompressor
infile = bz2.BZ2File("enwiki-latest-pages-articles.xml.bz2", "r")
output = bz2.BZ2File("text.xml", "w")
output.write(infile.read(5))
infile.close()
infile = bz2.BZ2File("enwiki-latest-pages-articles.xml.bz2", "r")
decompressor = bz2.BZ2Decompressor()
output = open("text.xml", "wb")
for i in range(10):
    output.write(decompressor.decompress(infile.read()))
infile.close()
output.close()
infile = bz2.BZ2File("enwiki-latest-pages-articles.xml.bz2", "r")
decompressor = bz2.BZ2Decompressor()
output = open("text.xml", "wb")
buffer_size = 32*1024
buffer = infile.read(buffer_size)
while len(buffer) > 0:
   
