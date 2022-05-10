fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__code__()


# In[ ]:


def f():
    pass

f.__code__.co_firstlineno


# In[ ]:


import sys
sys.version_info


# In[ ]:


sys.version_info[0]


# In[ ]:


import sys
if sys.version_info[0] < 3:
    import Tkinter
else:
    import tkinter as Tkinter


# In[ ]:


import sys
sys.platform


# In[ ]:


import os
os.environ['PATH']


# In[ ]:


import os
os.environ.get('FOO', 'bar')


# In[ ]:


import os
os.environ['PATH'] = '/bin:/usr/bin:/usr/local/bin'


# In[ ]:


import os
os.getenv('FOO', 'bar')


# In[ ]:


import os
os.getenv('FOO')


# In[ ]
