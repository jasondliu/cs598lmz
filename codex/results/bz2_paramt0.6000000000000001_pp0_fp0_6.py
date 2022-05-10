from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh91AY&SY\xd8\xee\x9a\x04\x00\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

# In[ ]:


import bz2
bz2.decompress(b'BZh91AY&SY\xd8\xee\x9a\x04\x00\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

# In[ ]:


from urllib.request import urlopen
with urlopen('http://www.pythonchallenge.com/pc/def/integrity.html') as story:
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split
