import bz2
# Test BZ2Decompressor

bz2_file = '../../data/sample.bz2'

decompressor = bz2.BZ2Decompressor()

with open(bz2_file, 'rb') as f:
    content = f.read()

content_decompressed = decompressor.decompress(content)
print(content_decompressed)

# Test BZ2File

bz2_file = '../../data/sample.bz2'

with bz2.BZ2File(bz2_file, 'r') as f:
    content = f.read()
    print(content)

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
