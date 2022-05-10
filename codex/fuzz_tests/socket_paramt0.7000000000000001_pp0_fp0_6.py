import socket
socket.if_indextoname('42')
```

This is a list of all the interfaces available on the system and an interface might be a physical ethernet card, a virtual interface, a wireless interface, or a VLAN.

```python
import netifaces
netifaces.interfaces()
```

We can see the IP address of the interface by using the `ifaddresses` method.

```python
import netifaces
netifaces.ifaddresses('en0')
```

This is a dictionary keyed on the different kinds of addresses, and each of them is a list of dictionaries. The first dictionary contains a key `addr` that contains the IP address as string.

```python
import netifaces
netifaces.ifaddresses('en0')[netifaces.AF_INET][0]['addr']
```

The second item in the list is for the broadcast address. The broadcast address is used to send data to all hosts in the subnet. It does so by sending a frame to the broadcast MAC address.

```python
import netifaces
netifaces.ifaddresses('
