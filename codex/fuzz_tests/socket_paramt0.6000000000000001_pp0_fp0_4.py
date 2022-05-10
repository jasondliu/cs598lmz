import socket
socket.if_indextoname(0)

socket.if_indextoname(2)

import netifaces
netifaces.interfaces()

netifaces.ifaddresses('en0')

netifaces.ifaddresses('en0')[netifaces.AF_INET]

netifaces.ifaddresses('en0')[netifaces.AF_INET][0]['addr']
