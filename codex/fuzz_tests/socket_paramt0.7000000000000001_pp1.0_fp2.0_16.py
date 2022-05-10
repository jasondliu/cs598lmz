import socket
socket.if_indextoname("3")
```

```
with open("/sys/class/net/eth0/address") as f:
    print(f.read())
```

```
import fcntl
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
return ':'.join(['%02x' % ord(char) for char in info[18:24]])
```

### 2.5.5 主机名

```
import socket
socket.gethostname()
```

```
import socket
socket.getfqdn()
```

```
import platform
platform.node()
```

### 2.5.6 内核信息

```
import platform
platform.platform()
```

```
import platform
platform.version()
```

```
