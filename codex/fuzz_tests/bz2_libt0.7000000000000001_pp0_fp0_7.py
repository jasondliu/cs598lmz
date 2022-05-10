import bz2
bz2.decompress(obama_bz2)

#print(obama_bz2)


# In[9]:


# Compress set of individual bytes
import bz2
original_data = b'This is the original text.'
print('Original     :', len(original_data), original_data)

compressed = bz2.compress(original_data)
print('Compressed   :', len(compressed), compressed)

decompressed = bz2.decompress(compressed)
print('Decompressed :', len(decompressed), decompressed)


# In[10]:


# Compress set of text by encoding to bytes first
import bz2
original_data = 'This is the original text.'
print('Original     :', len(original_data), original_data)

compressed = bz2.compress(original_data.encode('utf-8'))
print('Compressed   :', len(compressed), compressed)

decompressed = bz2.decompress(compressed).decode('utf-
