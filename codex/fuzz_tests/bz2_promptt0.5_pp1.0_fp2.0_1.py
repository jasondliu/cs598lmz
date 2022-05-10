import bz2
# Test BZ2Decompressor

decomp = bz2.BZ2Decompressor()

with open('enwiki-latest-pages-articles1.xml-p10p30302.bz2', 'rb') as f:
    data = f.read()
    print(decomp.decompress(data))

# Test BZ2File

with bz2.BZ2File('enwiki-latest-pages-articles1.xml-p10p30302.bz2') as f:
    for line in f:
        print(line)

# Test BZ2Compressor

comp = bz2.BZ2Compressor()

with open('enwiki-latest-pages-articles1.xml-p10p30302.bz2', 'rb') as f:
    data = f.read()
    data = comp.compress(data)
    data = comp.flush()
    print(data)
 

# Test BZ2Decompressor.decompress

decomp = bz2.BZ2Decompressor()

with open('enwiki
