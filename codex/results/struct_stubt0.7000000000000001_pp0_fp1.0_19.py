from _struct import Struct
s = Struct.__new__(Struct)

def fake_unpack(self, data):
    return (1, 2, 3)

# set the unpack function to our own one
s.unpack = fake_unpack

# unpack our data
s.unpack(data)

# try to modify our data
s.unpack(data)
```

```
None
```

```
```

```
None
```

```
```
