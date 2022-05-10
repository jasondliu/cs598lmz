from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# In[ ]:

import tarfile
with tarfile.open('/tmp/data.tar.xz') as f:
    f.extractall('/tmp')


# In[ ]:

import os
os.listdir('/tmp/data')


# In[ ]:

import os
os.listdir('/tmp/data/data')


# In[ ]:

import os
os.listdir('/tmp/data/data/train')


# In[ ]:

import glob
glob.glob('/tmp/data/data/train/*.jpg')


# In[ ]:

import pandas as pd
df = pd.read_csv('/tmp/data/data/train.csv')
df.head()


# In[ ]:

import os
os.listdir('/tmp/data/data/test')


# In[ ]:

import glob
glob.glob('/tmp/data/data/test/*.jpg')


# In[ ]:
