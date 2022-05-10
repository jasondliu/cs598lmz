from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)


# In[ ]:


import bz2
bz2_comp = bz2.BZ2Compressor()
result = bz2_comp.compress(b'i am a string that needs to be compressed')
result += bz2_comp.flush()
print(result)
bz2.decompress(result)


# In[12]:


import sys
import bz2
opener = bz2.open
if sys.platform.startswith('win'):
    class BZ2FileSub(bz2.BZ2File):
        def read1(self, n):
            return self.read(n)
    opener = lambda filename, mode, **kwargs: BZ2FileSub(filename, mode)
with opener('somefile.bz2', 'rt') as f:
    data = f.read()
