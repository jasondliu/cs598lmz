import socket
socket.if_indextoname(index)
```

```
socket.if_nameindex()
```

> 返回所有网络接口的索引和名字的列表，如果没有网络接口返回空列表

```
socket.gethostbyname(hostname)
```

> 返回主机名的IP地址

```
socket.gethostbyname_ex(hostname)
```

> 返回主机名的IP地址，同时返回一个列表，包含可能的别名，以及一个列表，包含主机名的所有IP地址

```
socket.
