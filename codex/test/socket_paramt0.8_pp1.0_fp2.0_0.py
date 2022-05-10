import socket
socket.if_indextoname(ifname)
ifname = socket.if_nameindex()[0][1]
print(ifname)

if ifname in netifaces.interfaces():
    print('%s is an interface on this system' % ifname)

print(netifaces.ifaddresses('lo0'))
print(netifaces.gateways())
print(netifaces.gateways()['default'])

import os
os.system('netstat -nrv')
