from types import FunctionType
list(FunctionType(f.__code__, {}).__globals__.keys())

#%%
import numpy as np
from numba import jit

@jit
def sum2d(arr):
    M, N = arr.shape
    result = 0.0
    for i in range(M):
        for j in range(N):
            result += arr[i,j]
    return result

a = np.arange(9).reshape(3,3)
print(sum2d(a))

#%%
import numpy as np
from numba import jit

@jit
def go_fast(a):
    trace = 0.0
    for i in range(a.shape[0]):
        trace += np.tanh(a[i,i])
    return a + trace

#%%
import numpy as np
from numba import jit

@jit
def go_fast(a):
    trace = 0.0
    for i in range(a.shape[0]):
        trace += np.tanh(a[i,i
