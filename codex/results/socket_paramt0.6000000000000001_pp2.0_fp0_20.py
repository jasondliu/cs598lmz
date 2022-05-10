import socket
socket.if_indextoname(3)
```

```
'en0'
```

```python
from socket import *
socket(AF_PACKET, SOCK_RAW, SOCK_RAW)
```

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.6/socket.py", line 189, in __init__
    _socket.socket.__init__(self, family, type, proto, fileno)
OSError: [Errno 93] Protocol not available
```

```python
from socket import *
s = socket(AF_PACKET, SOCK_RAW, htons(ETH_P_ALL))
```

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.6/socket.py", line 189, in __init__
    _socket.socket.__init__(self, family, type, proto, fileno)
OS
