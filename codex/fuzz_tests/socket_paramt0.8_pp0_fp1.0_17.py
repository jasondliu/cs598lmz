import socket
socket.if_indextoname(index)

# get all sockets
socket.socket_list()

# get all socket addresses
socket.socket_list([type])
```

```python
# get all interfaces addresses
for interface in interfaces():
    print(interface)
```

```python
# get all socket addresses
socket_list = socket.socket_list([socket.AF_INET])
for interface in socket_list:
    print(interface)
```

### Low level method

```python
import os
import fcntl
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
SIOCGIFADDR = 0x8915
for ifname in [b'lo', b'eth0']:
    ifreq = struct.pack('16si',ifname,socket.AF_INET)
    bytes = fcntl.ioctl(s.fileno(), SIOCGIFADDR, ifreq)
    host = socket.inet_ntoa(bytes[20:24])
    print(host)
```
