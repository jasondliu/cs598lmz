import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
gc.collect()
```

```python
>>> view
bytearray(b'\x00')
>>> view[0] = ord('a')
>>> view
bytearray(b'a')
```



## ctypes

```python
import ctypes

class Array(ctypes.Array):
    _type_ = ctypes.c_int
    _length_ = 3

c_array = Array()

view = memoryview(c_array)
```

```python
>>> view.format
'i'
>>> view.itemsize
4
>>> view.shape
(3,)
>>> view.strides
(4,)
```



## numpy.ndarray

```python
import numpy as np

array = np.zeros((3, 3))
view = memoryview(array)
```

```python
>>> view.format
'<f4'
>>> view.itemsize
4
>>> view.shape
(3, 3)
>>> view.strides
(12, 4
