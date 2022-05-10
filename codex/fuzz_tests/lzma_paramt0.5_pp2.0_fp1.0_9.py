from lzma import LZMADecompressor
LZMADecompressor().decompress(read_file('wiki.en.text.tar.lzma'))

# In[7]:


import tarfile
tar = tarfile.open('wiki.en.text.tar.lzma')
tar.extractall()

# In[8]:


import os
os.listdir()

# In[9]:


with open('wiki.en.text', 'r') as f:
    for line in f:
        print(line)
        break

# In[10]:


import re
def get_wiki():
    with open('wiki.en.text', 'r') as f:
        for line in f:
            line = re.sub('[^a-zA-Z]', ' ', line)
            line = line.lower()
            yield line

# In[11]:


wiki_gen = get_wiki()
next(wiki_gen)

# In[12]:


def get_wiki_articles():
    with open('wiki.en.text', 'r') as f:
        article = ''

