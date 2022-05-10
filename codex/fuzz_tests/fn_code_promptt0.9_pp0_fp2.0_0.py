fn = lambda: None
# Test fn.__code__

import pycuda.autoinit 
import pycuda.driver as drv
import numpy

from pycuda.compiler import SourceModule
mod = SourceModule(r"""

#include <stdio.h>

__global__ void func_1(int *arry){

  arry[0] *= 2;

}

""")

func_1 = mod.get_function("func_1")

arr = numpy.arange(100,dtype=numpy.int32)

arr2 = numpy.zeros_like(arr)

# copy numpy array to gpu
gpua = drv.mem_alloc(arr.nbytes)
drv.memcpy_htod(gpua,arr)
gpua2 = drv.mem_alloc(arr2.nbytes)
drv.memcpy_htod(gpua2,arr2)
print arr[:10]

func_1(
    gpua,
    block=(10,1,1),
    grid=(10,1,1)

