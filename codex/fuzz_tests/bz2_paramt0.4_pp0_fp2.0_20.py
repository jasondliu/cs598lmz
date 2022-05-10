from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# In[ ]:


# 使用bz2模块压缩数据
import bz2
bz2.compress(data)

# In[ ]:


# 使用bz2模块压缩数据
from bz2 import compress
compress(data)

# In[ ]:


# 使用bz2模块压缩数据
from bz2 import BZ2Compressor
BZ2Compressor().compress(data)

# In[ ]:


# 使用bz2模块压缩数据
from bz2 import BZ2Compressor
c = BZ2Compressor()
c.compress(data)
c.flush()

# In[ ]:


# 使用bz2模块压缩数据
