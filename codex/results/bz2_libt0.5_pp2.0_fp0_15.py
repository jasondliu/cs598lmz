import bz2
bz2_file = bz2.BZ2File('data/test.json.bz2', 'r')
bz2_file.readline()

# In[ ]:


import json
import pandas as pd
import numpy as np

def parse(path):
    g = gzip.open(path, 'r')
    for l in g:
        yield json.dumps(eval(l))

def getDF(path):
    i = 0
    df = {}
    for d in parse(path):
        df[i] = d
        i += 1
    return pd.DataFrame.from_dict(df, orient='index')

df = getDF('data/reviews_Cell_Phones_and_Accessories_5.json.gz')
df.head()

# In[ ]:


df.shape

# In[ ]:


df['reviewText'][0]

# In[ ]:


df['summary'][0]

# In[ ]:


df['overall'][0]

#
