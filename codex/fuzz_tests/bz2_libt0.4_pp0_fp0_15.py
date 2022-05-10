import bz2
bz2_file = bz2.BZ2File('wiki.txt.bz2')
data = bz2_file.read()
bz2_file.close()

data[0:60]

#%%
import gzip
gz_file = gzip.open('wiki.txt.gz', 'rb')
data = gz_file.read()
gz_file.close()

data[0:60]
