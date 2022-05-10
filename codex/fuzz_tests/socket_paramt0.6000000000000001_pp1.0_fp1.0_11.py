import socket
socket.if_indextoname(1)
# 'lo'
socket.if_indextoname(2)
# 'eth0'
socket.if_indextoname(3)
# 'eth1'
```

```python
import socket
socket.if_nametoindex('lo')
# 1
socket.if_nametoindex('eth0')
# 2
socket.if_nametoindex('eth1')
# 3
```

```python
import socket
socket.gethostbyname('localhost')
# '127.0.0.1'
socket.gethostname()
# 'hpc'
socket.getfqdn()
# 'hpc.local'
```

```python
import socket
socket.gethostbyaddr('127.0.0.1')
# ('localhost', [], ['127.0.0.1'])
```

```python
import socket
socket.getprotobyname('udp')
# 17
socket.getprotobyname('icmp')
# 1
socket.getprotobyname('tcp
