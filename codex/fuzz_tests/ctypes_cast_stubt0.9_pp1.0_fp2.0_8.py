import ctypes
ctypes.cast(0x12345678, ctypes.py_object).value = 123
print (c_int.from_address(0x12345678).value)
```

```
123
```

### File

```python
fd = os.open('/tmp/python.txt', os.O_RDWR|os.O_CREAT)
f = open(fd, 'w+')
print f.read()
f.write('hello, world')
f.flush()
f.seek(0)
print f.read()
os.close(fd)
```

```

hello, world
```

### Python object

```python
import objgraph
obj = objgraph.by_type('dict')[-1]

class MyClass(ctypes.Structure):
    pass
obj = MyClass()
MyClass._fields_ = [
    ('dict', ctypes.py_object)
]
obj.dict = {}

print ctypes.cast(id(obj), ctypes.py_object).value
print objgraph.by
