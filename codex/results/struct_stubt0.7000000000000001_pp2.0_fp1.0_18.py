from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("I 2s f")
s.size

```

```python
>>> s = Struct("I 2s f")
>>> s.size
12
```

```python
>>> import binascii
>>> binascii.hexlify(s.pack(7, b"spam", 3.0))
b'07000000736170603f0000000000000'
```

```python
>>> values = s.unpack(b'07000000736170603f0000000000000')
```


```python
>>> values
(7, b'sp', 3.0)
```

- 4 bytes for the integer: 0x07000000
- 2 bytes for the string: 0x73 0x61
- 4 bytes for the floating point: 0x03f00000

```python
>>> binascii.hexlify(s.pack(7, b"spam", 3.0))
b'07000000736170603f0000000000000'
```

```python
>>> s.pack(7, b"spam",
