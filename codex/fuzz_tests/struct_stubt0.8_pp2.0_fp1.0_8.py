from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<15sh'
s.size = s.unpack(bytes(30)).__sizeof__()
print(s.size)
# 30
>>> s.format = '<3sh'
>>> s.size = s.unpack(bytes(5)).__sizeof__()
>>> print(s.size)
5
```

### wtf

```python
>>> bytes(None)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    bytes(None)
TypeError: initial_bytes must be an iterable or integer, not NoneType
>>> None.__sizeof__()
8
>>> bytes(None.__sizeof__())
b'\x00\x00\x00\x00\x00\x00\x00\x00'
>>> bytes(bytes(None.__sizeof__()))
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    bytes(bytes(None.__sizeof__
