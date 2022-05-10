import socket
socket.if_indextoname()

2.6.2. Python 3

>>> print(socket.if_indextoname(1))
lo
>>> print(socket.if_indextoname(2))
eth0

```
## Using the struct module

```python
>>> import struct
>>> struct.pack(b'!I', 354)
b'\x00\x00\x01,
>>> struct.pack(b'!I', 354)[0]
0
>>> struct.pack(b'!I', 354)[1]
0
>>> struct.pack(b'!I', 354)[2]
1
>>> struct.pack(b'!I', 354)[3]
44
>>> struct.unpack(b'!I', b'\x00\x00\x01,
>>> struct.unpack(b'!I', b'\x00\x00\x01,')
(354,)
>>> struct.unpack(b'!I', b'\x00\x00\x01, ')
Traceback (most recent call last):
  File "", line 1
