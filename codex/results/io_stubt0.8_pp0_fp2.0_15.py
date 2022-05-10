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
view[0] = 42
gc.collect()
assert view[0] == 42
```

```python
import gc

class File(object):
    def read(self, size):
        return b''

f = File()
f.read(1)
f.buffer = File()
f.buffer.read(1)
del f

gc.collect()
```

```python
import gc

class File:
    def readinto(self, buf):
        raise NotImplementedError
    def readable(self):
        return True

f = File()
f.readinto(memoryview(bytearray(1)))
f.read(1)
f.readinto1(memoryview(bytearray(1)))
del f

gc.collect()
```

```python
class File:
    def readinto(self, buf):
        raise NotImplementedError
    def readable(self):
        return True

class SubFile(File):
    def readinto(self,
