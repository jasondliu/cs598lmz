import bz2
# Test BZ2Decompressor Object
#decompressor = bz2.BZ2Decompressor()
#decompressed_data = decompressor.decompress(compressed_data)
#decompressed_data
# Read bz2 compressed file
with bz2.open('data/enwiki-20160901-pages-articles-multistream.xml.bz2', 'rt') as f:
    first_line = f.readline()
    #print(first_line)
# Read bz2 compressed file
with bz2.open('data/enwiki-20160901-pages-articles-multistream.xml.bz2', 'rt') as f:
    for i, line in enumerate(f):
        print(line)
        if i > 2:
            break

# Read bz2 compressed file
with bz2.open('data/enwiki-20160901-pages-articles-multistream.xml.bz2', 'rt') as f:
    for line in f:
        print(line)
        break
# Read bz2 compressed file
with b
