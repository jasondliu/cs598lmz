import socket
socket.if_indextoname(2)

for interface in netifaces.interfaces():
    print(interface)
    print(netifaces.ifaddresses(interface))
    print('\n')
    #print(netifaces.ifaddresses(interface)[netifaces.AF_LINK])
    #print(netifaces.ifaddresses(interface)[netifaces.AF_INET])

#print(netifaces.ifaddresses('en0'))
