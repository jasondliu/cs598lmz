import socket
socket.if_indextoname(7)

# 或者

import netifaces
netifaces.ifaddresses('en0')[netifaces.AF_INET][0]['addr']
