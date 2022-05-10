import socket
socket.if_indextoname(1)

# 'en0'
```

## `if_nameindex`

```
>>> import socket
>>> socket.if_nameindex()
[(1, 'lo0'), (2, 'gif0'), (3, 'stf0'), (4, 'en0'), (5, 'en1'), (6, 'fw0'), (7, 'vmnet1'), (8, 'vmnet8')]
```

## `if_nametoindex`

```
>>> import socket
>>> socket.if_nametoindex('lo0')
1
```

## `gethostbyname`

```
>>> import socket
>>> socket.gethostbyname('www.python.org')
'82.94.164.162'
```

## `gethostbyname_ex`

```
>>> import socket
>>> socket.gethostbyname_ex('www.python.org')
('www.python.org', [], ['82.94.164.162'])
```

## `gethostbyaddr`

``
