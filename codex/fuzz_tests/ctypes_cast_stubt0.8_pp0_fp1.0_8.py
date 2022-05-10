import ctypes
ctypes.cast(p, ctypes.py_object).value
9
</code>
I want to pass that <code>ctypes.c_void_p</code> or <code>ctypes.c_void_p_p</code> to a function in another library which takes a <code>void *</code> (and <code>**</code>) and does C-style casts inside the function to a known type.  I've tried simply passing it and also casting it to a <code>ctypes.c_void_p</code> and/or <code>ctypes.c_void_p_p</code> but it fails with undefined symbol errors.  Is there any way to do this?
<code>from ctypes import *
import numpy as np

n = np.zeros(1, np.int)
print(n)
n[0] = 9
print(n[0])

p = cast(n.ctypes.data, c_void_p)
print(p)

# fails:
# undefined symbol: _ZN2myNS3fooEPv
# myNS.foo
