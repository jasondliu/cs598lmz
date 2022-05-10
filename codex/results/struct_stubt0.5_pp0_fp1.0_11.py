from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<I'
s.size = 4
s.unpack(b'\x00\x00\x00\x00')
```

## Unpacker

```python
from _struct import _unpack_int
_unpack_int(b'\x01\x00\x00\x00', 0, '<')
```

## Packer

```python
from _struct import _pack_int
_pack_int(1, '<')
```

## Lazy Struct

```python
from _struct import _lazystruct
_lazystruct('<I')(b'\x00\x00\x00\x00')
```

## Lazy Unpacker

```python
from _struct import _lazystruct
_lazystruct('<I').unpack(b'\x00\x00\x00\x00')
```

## Lazy Packer

```python
from _struct import _lazystruct
_lazystruct('<I').pack(
