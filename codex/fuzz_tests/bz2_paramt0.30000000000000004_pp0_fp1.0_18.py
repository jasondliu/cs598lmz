from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# In[ ]:


# We can also use the bz2 module to compress data. 
# The compress method returns the compressed data as a bytes object.

import bz2
original_data = b'This is the original text.'
print('Original     :', len(original_data), original_data)
compressed = bz2.compress(original_data)
print('Compressed   :', len(compressed), compressed)
decompressed = bz2.decompress(compressed)
print('Decompressed :', len(decompressed), decompressed)

# In[ ]:


# The bz2 module also contains a useful helper class called BZ2Compressor for 
# compressing data incrementally.

import bz2
compressor = bz2.BZ2Compressor()
print(compressor.compress(b'This is the original text.'))
print(compressor.flush())

# In[ ]:


# The zlib module provides a lower-level interface to many of the same 
# compression
