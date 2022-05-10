import socket
socket.if_indextoname('2')

socket.gethostbyname('localhost')

socket.gethostbyaddr('127.0.0.1')
```

```python
import netifaces
netifaces.interfaces()

netifaces.ifaddresses('eth0')
netifaces.ifaddresses('wlan0')
netifaces.ifaddresses('lo')

netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']

netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['netmask']

netifaces.ifaddresses('eth0')[netifaces.AF_LINK][0]['addr']

netifaces.ifaddresses('lo')[netifaces.AF_INET][0]['addr']

netifaces.ifaddresses('lo')

netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']

netifaces.ifaddresses('[34meth0
