import gc, weakref

import numpy as np
from numba import cuda, float32, float64, int32, int64, uint32, uint64
from numba.tests.support import TestCase
from numba.cuda.testing import skip_on_cudasim, unittest


class TestWeakRef(TestCase):
    def test_weakref_on_device_object(self):
        """
        Test that we can create weakref on device object.
        """
        @cuda.jit("void(float32[:, :])")
        def foo(x):
            pass

        d_arr = cuda.to_device(np.arange(10, dtype=np.float32).reshape(2, 5))
        wref = weakref.ref(d_arr)
        foo[1, 1](d_arr)
        del d_arr
        gc.collect()
        self.assertIsNone(wref())

    def test_weakref_on_stream(self):
        """
        Test that we can create weakref on CUDA stream.
       
