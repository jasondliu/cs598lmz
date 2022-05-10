import gc, weakref
import numpy as np

import pyopencl as cl
import pyopencl.characterize
import pyopencl.array

ctx = cl.create_some_context()
queue = cl.CommandQueue(ctx)
mf = cl.mem_flags

def print_buffers(a, b):
    print "a"
    for i in range(4):
        print a[i]
    print "b"
    for i in range(4):
        print b[i]

a_buf = cl.Buffer(ctx, mf.READ_ONLY, 16)
b_buf = cl.Buffer(ctx, mf.WRITE_ONLY, 16)

a = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], dtype=np.float32)
b = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], dtype=np
