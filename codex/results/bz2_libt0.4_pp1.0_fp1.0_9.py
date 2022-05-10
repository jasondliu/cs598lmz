import bz2
bz2.decompress(bz2_data)

#%%
import gzip
s = b'witch which has which witches wrist watch'
len(s)
t = zlib.compress(s)
len(t)
zlib.decompress(t)

#%%
import gzip
f = gzip.open('/home/ubuntu/workspace/test.txt.gz', 'wt')
f.write('"Hello, world!"')
f.close()

#%%
import gzip
f = gzip.open('/home/ubuntu/workspace/test.txt.gz', 'rt')
text = f.read()
f.close()

#%%
import bz2
f = bz2.open('/home/ubuntu/workspace/test.txt.bz2', 'wt')
f.write('"Hello, world!"')
f.close()

#%%
import bz2
f = bz2.open('/home/ubuntu/workspace/test.txt.bz2', 'rt')
text = f.read()

