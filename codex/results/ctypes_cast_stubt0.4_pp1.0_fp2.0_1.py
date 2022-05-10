import ctypes
ctypes.cast(0, ctypes.py_object)

# In[ ]:


# 가비지 컬렉션이 발생하는 시점을 조정하는 방법
import sys

n = 10
data = []

for i in range(n):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
    data.append(n)

# In[ ]:


# 가비지 컬렉션이 발생하는 시점을 조정하는 방법
import ctypes
import gc
import sys

def ref_count(address: int):
    return ctypes.c_long.from_
