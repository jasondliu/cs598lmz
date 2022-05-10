import socket
socket.if_indextoname(2)

import netifaces
netifaces.interfaces()
netifaces.ifaddresses('eth0')[netifaces.AF_INET]
