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

import gc
gc.collect()
print(view)
```

```
>>> import test
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "test.py", line 18, in <module>
    import gc
  File "test.py", line 19, in <module>
    gc.collect()
  File "test.py", line 20, in <module>
    print(view)
NameError: name 'view' is not defined
```

## test2.py

```
import io

class File(object):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

import gc
gc.collect()
print(view)
```

```
>>> import test2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
 
