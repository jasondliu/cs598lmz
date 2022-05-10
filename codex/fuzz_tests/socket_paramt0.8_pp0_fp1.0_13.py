import socket
socket.if_indextoname(0)
```

```
'eth0'
```

```
socket.if_indextoname(1)
```

```
'tun0'
```

> 获取所有ip

```
import netifaces as ni
ni.interfaces()
```

```
['lo', 'wlan0', 'eth0', 'tun0']
```

> 获取某个ip的所有信息

```
ni.ifaddresses('eth0')
```

```
{18: [{'addr': 'fe80::ba27:ebff:fe02:1d75', 'netmask': 'ffff:ffff:ffff:ffff::'}], 2: [{'broadcast': '192.168.1.255', 'addr': '192.168.1.101', 'netmask': '255.255.255.0'}]}
```



> 获取某个ip的
