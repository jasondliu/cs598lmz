import bz2
# Test BZ2Decompressor

bz2_decompressor = bz2.BZ2Decompressor()

with open('data/enwik8.bz2', 'rb') as f:
    file = f.read(100)
    result = bz2_decompressor.decompress(file)
    print(result)

with open('data/enwik8.bz2', 'rb') as f:
    for chunk in iter(lambda: f.read(100), b''):
        result = bz2_decompressor.decompress(chunk)
        #print(result)

 
# Test BZ2File

with bz2.BZ2File('data/enwik8.bz2', 'rb') as f:
    file = f.read(100)
    print(file)

with bz2.BZ2File('data/enwik8.bz2', 'rb') as f:
    for chunk in iter(lambda: f.read(100), b''):
        #print(chunk)
        pass
 

#
