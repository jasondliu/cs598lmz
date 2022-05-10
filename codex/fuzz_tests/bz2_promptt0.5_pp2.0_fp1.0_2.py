import bz2
# Test BZ2Decompressor

input_file = bz2.BZ2File('../data/enwiki-latest-pages-articles1.xml-p000000010p000030303.bz2')
output_file = open('../data/enwiki-latest-pages-articles1.xml-p000000010p000030303.xml', 'wb')
decompressor = bz2.BZ2Decompressor()

for data in iter(lambda : input_file.read(100 * 1024), b''):
    output_file.write(decompressor.decompress(data))

output_file.close()
input_file.close()
 
# Test BZ2Compressor

input_file = open('../data/enwiki-latest-pages-articles1.xml-p000000010p000030303.xml', 'rb')
output_file = bz2.BZ2File('../data/enwiki-latest-pages-articles1.xml-p000000010p000030303.bz2.test', 'wb')
compressor = bz2.BZ2Compressor(9)
