from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# In[ ]:


from zlib import decompress
decompress(data)

# In[ ]:


import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')

# In[ ]:


re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')

# In[ ]:


'tea for too'.replace('too', 'two')

# In[ ]:


import math
math.cos(math.pi / 4)

# In[ ]:


math.log(1024, 2)

# In[ ]:


import random
random.choice(['apple', 'pear', 'banana'])

# In[ ]:


random.sample(range(100), 10)

# In[ ]:


random.random()

# In[ ]:


random.randrange(6)

# In[ ]:


import statistics
data = [2.
