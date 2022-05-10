import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
ret = decompressor.decompress(compressed_data)
ret
import bz2
# Test BZ2File
with bz2.BZ2File('/tmp/compressed.bz2', 'wb') as f:
    f.write(compressed_data)  # Write compressed data

with bz2.BZ2File('/tmp/compressed.bz2', 'rb') as f:
    print(f.read())  # Read compressed data and decompress it
 
import bz2
# Test BZ2File
with bz2.BZ2File('/tmp/compressed.bz2', 'wb') as f:
    f.write(data)  # Write data and compress it

with bz2.BZ2File('/tmp/compressed.bz2', 'rb') as f:
    print(f.read())  # Read compressed data
 
 
 
 
 
 
 
 
 
 
 
 
 
