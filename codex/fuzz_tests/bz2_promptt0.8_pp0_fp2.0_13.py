import bz2
# Test BZ2Decompressor

data = b'BZh91AY&SY.\xc8N\x18\x00\x01>_\x80\x00\x10@\x02\xff\xf0\x01\x07n\x00?'
decomp = bz2.BZ2Decompressor()
decomp.decompress(data)
decomp.flush()
data = 'Ni ci ba sha lu du du du du du du du du du du du du'
len(data)
comp = bz2.BZ2Decompressor()
decomp.decompress(data)
decomp.flush()

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
import gzip
with gzip.open('myfile.gz', 'wt') as f:
    f.write(data)


 
with gzip.open('myfile.gz', 'rt') as f:
   
