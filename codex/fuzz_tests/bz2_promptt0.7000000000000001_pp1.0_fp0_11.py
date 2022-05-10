import bz2
# Test BZ2Decompressor

with open('test.bz2') as f:
    
    # we need to read the first byte to initialize BZ2Decompressor
    f.read(1)
    
    decompressor = bz2.BZ2Decompressor()
    
    # read all compressed data
    data = f.read()
    
    # decompress
    print(decompressor.decompress(data))

# Test BZ2File

with bz2.BZ2File('test.bz2') as f:
    print(f.read())

 

# Test BZ2File

with bz2.BZ2File('test.bz2') as f:
    
    # read all data
    data = f.read()
    
    # decompress
    print(bz2.decompress(data))


 

# Test BZ2File

with bz2.BZ2File('test.bz2') as f:
    
    # read all data
    data = f.read()
    
    #
