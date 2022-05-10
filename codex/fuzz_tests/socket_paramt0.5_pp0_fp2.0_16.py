import socket
socket.if_indextoname(7)

# 或者

import netifaces
netifaces.ifaddresses('en0')[netifaces.AF_INET][0]['addr']
```

```
>>> socket.gethostbyname(socket.gethostname())
'192.168.1.108'

>>> netifaces.ifaddresses('en0')[netifaces.AF_INET][0]['addr']
'192.168.1.108'
```

## 参考

[https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib](https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib)

[https://stackoverflow.com/questions/24196932/how-can-i-get-the-ip-address-of-eth0-in-python](https://stackoverflow.com/questions/24196932/how-can-i-
