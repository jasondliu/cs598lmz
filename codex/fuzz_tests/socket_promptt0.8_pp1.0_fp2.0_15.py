import socket
# Test socket.if_indextoname from netifaces
ifname = socket.if_indextoname(1)
print (ifname)
# Output: 'lo'
print ("\n")
# Test netifaces.ifaddresses from netifaces
import netifaces
print (netifaces.interfaces())
# Output: ['lo', 'eth0', 'wlan0']
print ("\n")
print (netifaces.ifaddresses('lo'))
# Output: {2: [{'addr': '127.0.0.1', 'netmask': '255.0.0.0'}], 10: [{'addr': '::1', 'netmask': 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff'}]}
print ("\n")
print (netifaces.ifaddresses('eth0'))
# Output: {2: [{'addr': '1.2.3.4', 'netmask': '255.255.255.0', 'broadcast': '1.2.3.255'}], 10: [{'addr': 'fe80::c
