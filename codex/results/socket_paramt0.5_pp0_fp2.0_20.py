import socket
socket.if_indextoname(3)
```

`socket.if_indextoname(3)` returns the name of the network interface associated with the index 3.

```python
import socket
socket.if_nameindex()
```

`socket.if_nameindex()` returns a list of (index, name) tuples.

```python
import socket
socket.gethostbyname('google.com')
```

`socket.gethostbyname('google.com')` returns the IPv4 address of the host google.com.

```python
import socket
socket.gethostbyname_ex('google.com')
```

`socket.gethostbyname_ex('google.com')` returns a tuple (hostname, aliases, ip_addresses) for the hostname google.com.

```python
import socket
socket.gethostbyaddr('216.58.206.68')
```

`socket.gethostbyaddr('216.58.206.68')` returns a tuple (hostname, aliases, ip_addresses) for the IP address 216.
