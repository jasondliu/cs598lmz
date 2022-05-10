from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

# In[ ]:


# Compress a string with bz2
import bz2

string = b"This is a string to compress"
compressed = bz2.compress(string)
print(compressed)

# In[ ]:


# Decompress a string with bz2
import bz2

compressed = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
decompressed = bz2.decompress(compressed)
print(decompressed)

# In
