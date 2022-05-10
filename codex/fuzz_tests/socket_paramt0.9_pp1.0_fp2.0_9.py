import socket
socket.if_indextoname('4')

```

```
>>> import socket
socket.if_nameindex()
# 得到网卡索引和名称的元组数组
[(1, 'lo'), (2, 'wlan0'), (3, 'eth0'), (4, 'any')]
locals()['_[1]']
# 返回当前的网卡索引和名称的字典
{1: (1, 'lo'), 2: (2, 'wlan0'), 3: (3, 'eth0'), 4: (4, 'any')}
```
