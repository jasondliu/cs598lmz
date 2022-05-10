from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# In[ ]:


# I'm not sure if this works, but it seems like it might
# https://stackoverflow.com/questions/29649944/how-to-extract-a-tar-file-in-memory-using-python
import io
import tarfile
tarobj = tarfile.open(fileobj=io.BytesIO(data))
tarobj.extractall()

# In[ ]:


# I'm not sure if this works, but it seems like it might
# https://stackoverflow.com/questions/29649944/how-to-extract-a-tar-file-in-memory-using-python
import io
import tarfile
tarobj = tarfile.open(fileobj=io.BytesIO(data))
tarobj.extractall()

# In[ ]:


# I'm not sure if this works, but it seems like it might
# https://stackoverflow.com/questions/29649944/how-to-extract-a-tar-file-in-
