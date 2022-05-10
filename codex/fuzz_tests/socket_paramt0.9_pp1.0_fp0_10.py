import socket
socket.if_indextoname(index)

#save the configuration
wifi.ifconfig(config=('192.168.1.1', '255.255.255.0', '192.168.1.100', '192.168.1.1'))

#set an ip on a network
wifi.ifconfig(config=('192.168.1.1', '255.255.255.0', '192.168.1.100', '0.0.0.0'))

#obtain ip addresses of application
socket.getaddrinfo('www.micropython.org', 80)

#determine host
socket.gethostbyname('www.micropython.org')


#socket programming
#sequential interface
#byte buffer oriented
#event-driven interface
#routing, fragmentation and reassembly

import uselect
import ustruct

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ADDR = socket.getaddrinfo('micropython.org', 80)[0][-1]

s.sendto(b'GET
