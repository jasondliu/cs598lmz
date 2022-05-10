import bz2
bz2_file = bz2.BZ2File('example.bz2')
data = bz2_file.read()
bz2_file.close()
data

# In[16]:

import gzip
with gzip.open('example.txt.gz', 'rt') as input_file:
    print(input_file.read())

# In[17]:

import bz2
with bz2.open('example.bz2', 'rt') as input_file:
    print(input_file.read())

# In[18]:

import gzip
with gzip.open('example.txt.gz', 'wt') as output_file:
    output_file.write('Contents of the example file go here.\n')

# In[19]:

import bz2
with bz2.open('example.bz2', 'wt') as output_file:
    output_file.write('Contents of the example file go here.\n')

# In[20]:

with gzip.open('example.txt.gz',
