import ctypes
ctypes.cast(buff, ctypes.py_object).value

#%%

import numpy as np
from numba import cuda
import time

# Controls threads per block and shared memory usage.
# The computation will be done on blocks of TPBxTPB elements.
TPB = 16

@cuda.jit
def fast_matmul(A, B, C):
    # Define an array in the shared memory
    # The size and type of the arrays must be known at compile time
    sA = cuda.shared.array(shape=(TPB, TPB), dtype=float32)
    sB = cuda.shared.array(shape=(TPB, TPB), dtype=float32)

    x = cuda.blockIdx.x
    y = cuda.blockIdx.y
    tx = cuda.threadIdx.x
    ty = cuda.threadIdx.y

    bpg = cuda.grid(1)    # number of total blocks

    if x >= C.shape[0] and y >= C.shape[1]:
        # Quit
