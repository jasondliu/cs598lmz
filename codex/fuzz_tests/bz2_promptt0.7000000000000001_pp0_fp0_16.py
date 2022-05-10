import bz2
# Test BZ2Decompressor

# Read file

with open('temp/data/enwiki-latest-pages-articles.xml.bz2', 'rb') as f:
    data = bz2.BZ2File(f)
    
    # Decompress
    decompressor = bz2.BZ2Decompressor()
    content = decompressor.decompress(data.read())
    
    # Print
    print(content[:1000])
 
# Test BZ2Compressor

# Read file

with open('temp/data/enwiki-latest-pages-articles.xml.bz2', 'rb') as f:
    data = bz2.BZ2File(f)
    
    # Compress
    compressor = bz2.BZ2Compressor()
    compressed = compressor.compress(data.read())
    
    # Print
    print(compressed[:1000])
 
# Read file

with open('temp/data/enwiki-latest-pages-articles.xml.bz2', 'rb') as f:
    # Compress

