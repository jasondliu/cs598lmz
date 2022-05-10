import socket
socket.if_indextoname(3)

In [14]: socket.if_indextoname(3)
Out[14]: 'eth0'

In [15]: socket.if_nameindex()
Out[15]: [(1, 'lo'), (2, 'eth0'), (3, 'eth1')]
```

```py
In [17]: import ctypes
In [18]: import ctypes.util
In [19]: libc = ctypes.CDLL(ctypes.util.find_library("c"))
In [20]: libc
Out[20]: <CDLL 'libc.so.6', handle 47633f60 at 7fc5c5e0b5f0>
In [21]: libc.if_nametoindex("eth0")
Out[21]: 3
```

## 参考
- [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html)
- [codewatch/libc-if_nameindex: libc if_nameindex API implementation for Python](https://github
