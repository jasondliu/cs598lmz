import socket
socket.if_indextoname(1)
```

```
'eth0'
```

The name of the socket can be used to access the socket object, and the object can be used to get the addresses associated with the socket.

```python
eth0 = socket.if_nameindex()[2][1]
eth0
```

```
'eth0'
```

```python
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect((eth0, 0))
```

```python
sock.getsockname()
```

```
('192.168.1.101', 0)
```

### Socket options

The socket object can be used to set and get socket options. Options are set by calling the `setsockopt()` method on the socket object.

```python
sock.setsockopt(socket.SOL_IP, socket.IP_TTL, 64)
```

The value of an option can be read with the `getsockopt()` method.
