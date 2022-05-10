import bz2
bz2.BZ2File(filepath)

# In[ ]:


# open the file with bz2.open
with bz2.open(filepath) as file:
    print(file.readline())

# In[ ]:


# read the file into a DataFrame with pandas
import pandas as pd
df = pd.read_csv(filepath, compression='bz2')
df.head()

# In[ ]:


# write to a compressed file
df.to_csv('data/titanic_filtered.csv.bz2', index=False, compression='bz2')

# In[ ]:


# create a gzip compressed file
import gzip
with gzip.open('data/titanic_filtered.csv.gz', 'wt') as f:
    f.write('"a","b","c"\n"1","2","3"\n')

# In[ ]:


# read from a compressed file
with gzip.open('data/titanic_filtered.csv.gz',
