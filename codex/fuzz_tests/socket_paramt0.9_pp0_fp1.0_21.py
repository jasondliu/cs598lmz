import socket
socket.if_indextoname('1')
#> 'en0'
```
## Get the network interface name and details

Below is a function that will return a dictionary of the network interfaces and their details.


```python
import socket
import fcntl
import struct
import os

def get_network_inteface_details():
    network_interface_details = {}
    connected_network_intefaces = get_connected_network_intefaces()
    for interface in connected_network_intefaces:
        if interface == 'lo':
            continue
        gw = os.popen("ip -4 route show default via %s" % (interface_gateway)).read().split()
        ip = socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', interface[:15])
        )[20:24])
        mask = socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            35099,  # SIOCGIF
