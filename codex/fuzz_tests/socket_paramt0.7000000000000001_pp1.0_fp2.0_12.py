import socket
socket.if_indextoname(2)
```

```
'eth0'
```

```
socket.if_indextoname(3)
```

```
'lo'
```

```
socket.if_indextoname(4)
```

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: socket.if_indextoname(4) failed
```


`if_nameindex()` returns a list of (index, name) tuples for all interfaces.

```
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.if_nameindex()
```

```
[(1, 'lo'), (2, 'eth0')]
```

#### 2.3.3.1.1. Socket Types

* `SOCK_STREAM`（`TPC`）
* `SOCK_DGRAM`（`UDP`）

