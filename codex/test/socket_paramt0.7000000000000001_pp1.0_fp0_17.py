import socket
socket.if_indextoname(2)

#Now we can use the interface name in our configuration
#to find the index we are looking for

[...]

#this will print the index of the interface eth0
print(netifaces.ifaddresses('eth0')[netifaces.AF_LINK][0]['addr'])

#this will print the index of the interface eth1
print(netifaces.ifaddresses('eth1')[netifaces.AF_LINK][0]['addr'])
