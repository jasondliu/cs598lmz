import socket
socket.if_indextoname('3')

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('0.0.0.0', 0))
s.connect(('8.8.8.8', 0))
s.getsockname()[0]

# pip install netifaces
import netifaces
netifaces.interfaces()

netifaces.ifaddresses('lo')

netifaces.ifaddresses('lo').get(netifaces.AF_INET)

netifaces.ifaddresses('lo').get(netifaces.AF_INET)[0]['addr']
