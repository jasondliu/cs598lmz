from types import FunctionType
list(FunctionType(FunctionType.__code__, {}))

# In[ ]:


# %load C:\Users\Asus\PYTHON_PROJECTS\PYTHON_WORKBOOK\Packages\Collections\collections_namedtuple.py
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
Point.x
Point.y

# In[ ]:


# %load C:\Users\Asus\PYTHON_PROJECTS\PYTHON_WORKBOOK\Packages\Collections\collections_deque.py
from collections import deque
deque(list(range(10)))

# In[ ]:


# %load C:\Users\Asus\PYTHON_PROJECTS\PYTHON_WORKBOOK\Packages\Collections\collections_defaultdict.py
from collections import defaultdict
d = defaultdict(list)
d
d['a']
d['a'].append(1)
d['a'].append(2)
d['a'].append
