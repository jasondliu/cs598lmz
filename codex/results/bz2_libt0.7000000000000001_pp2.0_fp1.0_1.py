import bz2
bz2.decompress(open("input.txt.bz2").read())[:20]

# In[23]:

open("input.txt").read()[:20]

# In[24]:

import gzip
gzip.decompress(open("input.txt.gz").read())[:20]

# In[25]:

import zipfile
z = zipfile.ZipFile("input.zip")
z.namelist()

# In[26]:

z.extract("input.txt")

# In[27]:

# Let's look at the Wikipedia article on Monty Python:

import requests
r = requests.get("http://en.wikipedia.org/wiki/Monty_Python")

# In[28]:

r.status_code

# In[29]:

r.headers['content-type']

# In[30]:

r.encoding

# In[31]:

r.text[:1000]

# In[32]:

from lxml import etree
tree = etree.HTML
