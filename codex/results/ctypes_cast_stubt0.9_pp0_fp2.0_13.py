import ctypes
ctypes.cast(x, ctypes.py_object).value = 10
ctypes.cast(y, ctypes.py_object).value = 20
ctypes.cast(z, ctypes.py_object).value = 30

# Step 1
for i in range(10):
    x = y
    y = z
    z = x + y

# Step 2
expected = x + y
r = z
print(r == expected) # Prints "True"

```

```python
# Example 2
import numpy as np
import ctypes
x = np.zeros((3,3), dtype=np.float64)
y = np.zeros((3,3), dtype=np.float64)
z = np.zeros((3,3), dtype=np.float64)

ctypes.cast(x, ctypes.py_object).value = 10
ctypes.cast(y, ctypes.py_object).value = 20
ctypes.cast(z, ctypes.py_object).value = 30

for i in range(10):
   
