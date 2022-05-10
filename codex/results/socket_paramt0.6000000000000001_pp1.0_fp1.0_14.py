import socket
socket.if_indextoname(4)

# Python 3.x
import netifaces
netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']

# Python 2.x
import netifaces
netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']

# Python 2.6+
import netifaces
netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']
