import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_float, ctypes.c_int)
f = FUNTYPE(lambda x: x*x)
f(3)

# functools.partial
from functools import partial
f = partial(lambda x: x*x, 3)
f()

# Numpy
import numpy as np
f = np.vectorize(lambda x: x*x)
f([1,2,3])

# List comprehensions
f = [lambda x: x*x for i in range(3)]
f[2](4)

# Dictionaries
f = {i:lambda x: x*x for i in range(3)}
f[2](4)
```
