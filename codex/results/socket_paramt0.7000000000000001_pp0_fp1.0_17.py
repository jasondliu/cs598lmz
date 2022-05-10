import socket
socket.if_indextoname(0)

# MacOSX
>>> import socket
>>> socket.if_nameindex()
[(1, 'lo0'), (2, 'gif0'), (3, 'stf0'), (4, 'en0'), (5, 'en1'), (6, 'fw0'), (7, 'vmnet1'), (8, 'vmnet8')]
>>>
>>> socket.if_indextoname(4)
'en0'
```

```
>>> import platform
>>> platform.system()
'Darwin'
```

```
>>> import platform
>>> platform.system()
'Windows'
```

```
>>> import platform
>>> platform.system()
'Linux'
```

```
>>> import platform
>>> platform.system()
'Linux'
```


## 端口号

```
>>> import socket
>>> server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
>>> server.bind(('0.0.0.0', 8888))
>>> server.list
