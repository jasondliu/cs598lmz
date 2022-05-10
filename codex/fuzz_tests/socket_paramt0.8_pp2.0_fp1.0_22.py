import socket
socket.if_indextoname(5)

# pip install netifaces
import netifaces
netifaces.interfaces()
netifaces.ifaddresses('lo0')
netifaces.ifaddresses('lo0')[netifaces.AF_INET]

# pip install netifaces-py3
import netifaces
netifaces.interfaces()
netifaces.ifaddresses('lo0')[netifaces.AF_INET][0]['addr']
netifaces.ifaddresses('lo0')[netifaces.AF_INET][0]['mask']
netifaces.gateways()
