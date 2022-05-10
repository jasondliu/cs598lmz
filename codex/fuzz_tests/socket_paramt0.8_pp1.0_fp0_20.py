import socket
socket.if_indextoname(2)  # False
socket.if_indextoname(3)  # b'\xe0\x4f\xd0\xe7\x8b\x08'
```

### Get all interfaces
Show all network interfaces and their index
```py
>>> import socket
>>> socket.if_nameindex()
[(1, b'lo'), (2, b'eth0'), (3, b'wlan0')]
```

## Source address
The source address of a socket can be retrieved using ``getsockname()``
```py
>>> import socket
>>> s = socket.socket()
>>> s.connect(("www.example.com", 80))
>>> s.getsockname()
("192.168.178.28", 55990)
```

## Getting the IP address from a hostname
Use [gethostbyname()](https://docs.python.org/3/library/socket.html#socket.gethostbyname) for this.
```py
>>> import socket
>>> socket.gethostbyname("www.example.com")
'93
