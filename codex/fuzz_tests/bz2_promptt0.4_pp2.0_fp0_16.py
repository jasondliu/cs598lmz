import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('sample.bz2', 'rb') as f_in, open('sample.txt', 'wb') as f_out:
    f_out.write(decompressor.decompress(f_in.read()))
# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('sample.txt', 'rb') as f_in, open('sample.bz2', 'wb') as f_out:
    f_out.write(compressor.compress(f_in.read()))
    f_out.write(compressor.flush())

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

