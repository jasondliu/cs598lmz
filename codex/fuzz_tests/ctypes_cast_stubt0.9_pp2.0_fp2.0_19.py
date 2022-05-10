import ctypes
ctypes.cast(merged, ctypes.py_object).value = a
print(merged)  # [1,1,2,2,3,3,4]
</code>
(In Python 3 it's just <code>merged[:] = a</code>.)
With numpy arrays you can't overwrite in-place the entire array like this (even with slicing, so <code>merged[:] = a</code> doesn't work either). Possible workarounds are listed in How do I reset a numpy array to all zeros?.

