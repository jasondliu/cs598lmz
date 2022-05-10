import bz2
# Test BZ2Decompressor

input_file = bz2.BZ2File('data/frwiki/frwiki-latest-pages-articles.xml.bz2')
decompressor = bz2.BZ2Decompressor()

output = b""
for block in iter(lambda: input_file.read(100 * 1024), b""):
    output += decompressor.decompress(block)
    
with open('data/frwiki/frwiki-latest-pages-articles.xml', 'wb') as f:
    f.write(output)

# Test BZ2Compressor

input_file = open('data/frwiki/frwiki-latest-pages-articles.xml', 'rb')

compressor = bz2.BZ2Compressor()

output = b""
for block in iter(lambda: input_file.read(100 * 1024), b""):
    output += compressor.compress(block)
    
with open('data/frwiki/frwiki-latest-pages-articles.xml.bz2', 'wb') as f:
    f.write(output)
