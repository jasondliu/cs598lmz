import bz2
# Test BZ2Decompressor() class.
decompress = bz2.BZ2Decompressor()

# Read data from decompressor object.
data = bz2.decompress(decompress)

# print reconcatenated data
data

# Using above method to decompress single line in the downloaded file. 
with open ('enwiki-latest-pages-articles-multistream1.xml-p10p30302.bz2', 'rb') as f:
    for line in iter(lambda : f.read(1024*1024), b''):
        decompress = bz2.BZ2Decompressor().decompress(f)
        if(decompress):
            print(decompress)

# Another way to decompress single line in the downloaded file. 
with bz2.BZ2File(r"enwiki-latest-pages-articles-multistream1.xml-p10p30302.bz2", "r") as f:
    for line in iter(lambda : f.readline(), b''):
        print(line)

# Try to decomp
