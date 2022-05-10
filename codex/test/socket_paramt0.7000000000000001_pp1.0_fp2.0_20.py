import socket
socket.if_indextoname(netifaces.ifaddresses(netifaces.interfaces()[1])[netifaces.AF_INET][0]['addr'])
