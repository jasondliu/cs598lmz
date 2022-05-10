import socket
# Test socket.if_indextoname
print socket.if_indextoname(1)
# Test socket.if_nameindex
print socket.if_nameindex()
```

```
lo0
[(1, 'lo0'), (2, 'en0')]
```

## socket.if_nameindex()

Return a list of network interface information. Each element of the list is a tuple consisting of an interface index and the associated interface name.

```python
import socket
print socket.if_nameindex()
```

```
[(1, 'lo0'), (2, 'en0')]
```

## socket.if_nametoindex(if_name)

Return the interface index corresponding to the given interface name.

```python
import socket
print socket.if_nametoindex('lo0')
```

```
1
```

## socket.inet_aton(ip_string)

Convert an IPv4 address from dotted-quad string format (for example, ‘123.45.67.89’) to 32-bit packed binary format
