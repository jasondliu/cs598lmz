fn = lambda: None
gi = (i for i in ())
fn.__code__ = fn.__code__.__bases__ = (1,)
print(fn()())"""

test_np_arange_slice_negative_step = """
import numpy as np
a = np.arange(10)
print(a[:-1:2])"""

test_np_arange_slice_negative_step_after = """
import numpy as np
a = np.arange(10)
print(a[1::-2])"""

test_using_multiple_cs = """
import numpy as np
a = np.arange(10)

# A different code source.
class Point:
    def __init__(self, x):
        self.x = x

# A different code source.
class CSlice:
    def __init__(sself, start, stop, step):
        sself.start = start
        sself.stop = stop
        sself.step = step

# Compiles with the others in the same code source.
print(a[Point(1):CSlice(int, None, None)])"""
