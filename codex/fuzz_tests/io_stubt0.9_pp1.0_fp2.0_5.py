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

view[0] = ord("a")
```

```python
def f(x):
    x = 8

cst = dis.Bytecode(f)
for x in cst.dis():
    print(x)

  1           0 LOAD_CONST               1 (8)
              2 STORE_FAST               0 (x)
              5 LOAD_CONST               0 (None)
              7 RETURN_VALUE        
```

## Call

```python
print("a")
```

```python
import dis
def f(x):
    x = 8

cst = dis.Bytecode(f)
for x in cst.dis():
    print(x)
```

```
  1           0 LOAD_CONST               1 (8)
              2 STORE_FAST               0 (x)
              5 LOAD_CONST               0 (None)
              7 RETURN_VALUE        
```

```python
import dis as d
import types
dis = types.ModuleType("dis")

