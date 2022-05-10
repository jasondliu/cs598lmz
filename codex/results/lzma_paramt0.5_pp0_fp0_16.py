from lzma import LZMADecompressor
LZMADecompressor().decompress(test_data)

# In[ ]:


#decompress_data = LZMADecompressor().decompress(compressed_data)
#print(len(decompress_data))


# In[ ]:


#import sys
#print("{} Kb".format(sys.getsizeof(decompress_data)/1024))


# In[ ]:


#import pickle
#pickle.dump(decompress_data, open("data_decompress.p", "wb"))


# In[ ]:


import pickle
data = pickle.load(open("data_decompress.p", "rb"))
len(data)


# In[ ]:


import numpy as np
data = np.frombuffer(data, dtype=np.uint8).astype(np.float32)
data.shape


# In[ ]:


data = data.reshape(10000, 3072)
data.shape


# In[ ]:


#data[0]


# In[
