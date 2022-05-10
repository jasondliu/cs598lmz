from lzma import LZMADecompressor
LZMADecompressor.decompress(data)

# In[ ]:


import tarfile
import os

def untar(fname):
    if (fname.endswith("tar.gz")):
        tar = tarfile.open(fname)
        tar.extractall()
        tar.close()
        print("Extracted in Current Directory")
    else:
        print("Not a tar.gz file: '%s '" % sys.argv[0])
        
untar('/kaggle/input/nlp-getting-started/train.csv.zip')
untar('/kaggle/input/nlp-getting-started/test.csv.zip')

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# In[ ]:


df_train = pd.read_csv('train.csv')
df_test = pd.read_csv('test.csv')

# In[ ]:


df_train.head()
