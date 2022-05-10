from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed)

# In[ ]:


#Compress the file
import lzma
with lzma.open("lzma_compressed_file.xz", "wb") as f:
    f.write(b"Hello")

# In[ ]:


#Decompress the file
import lzma
with lzma.open("lzma_compressed_file.xz") as f:
    file_content = f.read()

# In[ ]:


#Compress the file
import lzma
with lzma.open("lzma_compressed_file.xz", "w") as f:
    f.write("Hello".encode("utf-8"))

# In[ ]:


#Decompress the file
import lzma
with lzma.open("lzma_compressed_file.xz") as f:
    file_content = f.read()

# In[ ]:


import lzma
with lzma.open("lzma_compressed
