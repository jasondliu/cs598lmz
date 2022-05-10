import ctypes
ctypes.cast(0, ctypes.py_object).value

# In[ ]:


# %load_ext Cython
# %%cython

import numpy as np
cimport numpy as np

def get_pairs(int[:,:] A):
    cdef int N = A.shape[0]
    cdef int i, j
    cdef int[:,:] pairs = np.empty((N*(N-1)//2, 2), dtype=np.int32)
    cdef int k = 0
    for i in range(N):
        for j in range(i+1, N):
            pairs[k, 0] = i
            pairs[k, 1] = j
            k += 1
    return pairs

# In[ ]:


# %load_ext Cython
# %%cython

import numpy as np
cimport numpy as np

def get_pairs(int[:,:] A):
    cdef int N = A.shape[0]
    cdef int i, j
    cdef int[:,:] pairs =
