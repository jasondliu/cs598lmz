import socket
socket.if_indextoname(3)
```

### Get the IP address of a certain interface
```python
import socket
socket.if_nameindex()
```

### Retrieve the list of active interfaces on the host
```python
import netifaces
netifaces.interfaces()
```

### Retrieve an interface's IP addresses
```python
import netifaces
netifaces.ifaddresses('lo')
```

### Get all IP addresses of the host
```python
import netifaces
netifaces.ifaddresses('lo')
```

### Retrieve a specific address information of a certain interface
```python
import netifaces
netifaces.ifaddresses('eth1')[netifaces.AF_INET][0]['addr']
```

### Get the IP address of the default gateway for a network interface
```python
import netifaces
netifaces.gateways()
```

### Get the default gateway address
```python
import netifaces
netifaces.gateways()['default'][netifaces.AF_
