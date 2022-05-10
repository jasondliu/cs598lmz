import lzma
lzma.decompress(compressed)

# In[ ]:


# Compress a file
import lzma
with open('file.txt', 'rb') as f_in, lzma.open('file.txt.xz', 'wb') as f_out:
    f_out.writelines(f_in)

# In[ ]:


# Decompress a file
import lzma
with lzma.open('file.txt.xz') as f_in, open('file.txt', 'wb') as f_out:
    f_out.write(f_in.read())

# In[ ]:


# Compress a file
import lzma
with open('file.txt', 'rb') as f_in, lzma.open('file.txt.xz', 'w') as f_out:
    f_out.write(f_in.read())

# In[ ]:


# Decompress a file
import lzma
with lzma.open('file.txt.xz') as f_in
