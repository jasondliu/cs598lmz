from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack_from(b'\x01\x00\x00\x00')

# Deserialization
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack_from(b'\x01\x00\x00\x00')
```

## `_thread`

### `_local`

```python
# Serialization
from _thread import local
l = local.__new__(local)

# Deserialization
from _thread import local
l = local.__new__(local)
```

## `_weakref`

### `ref`

```python
# Serialization
from _weakref import ref
r = ref.__new__(ref)
r.__init__(lambda: None)

# Deserialization
from _weakref import ref
r = ref.__new__(ref)
r.__init__(lambda: None)
```

### `proxy`

``
