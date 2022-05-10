import socket
socket.if_indextoname(3)

# result
# 'enp0s3'

```

```python
import socket
socket.if_nametoindex('enp0s3')

# result
# 3

```

```python
import socket
socket.getaddrinfo('localhost', 80)

# result
# [(<AddressFamily.AF_INET6: 30>, <SocketKind.SOCK_STREAM: 1>, 6, '', ('::1', 80, 0, 0)),
#  (<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_STREAM: 1>, 6, '', ('127.0.0.1', 80))]

```

```python
import socket
socket.gethostbyname('localhost')

# result
# '127.0.0.1'

```

```python
import socket
socket.gethostbyname_ex('localhost')

# result
# ('localhost', [], ['127.0.0.1'])

```

```python
import socket
socket
