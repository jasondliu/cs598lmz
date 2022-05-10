import socket
socket.if_indextoname(12)

#if_nameindex
import socket
socket.if_nameindex()

#if_nametoindex
import socket
socket.if_nametoindex(b'wlan0')

#inet_aton
import socket
socket.inet_aton('192.168.1.1')

#inet_ntoa
import socket
socket.inet_ntoa(b'\xc0\xa8\x01\x01')

#ntohl
import socket
socket.ntohl(0xc0a80101)

#ntohs
import socket
socket.ntohs(0x0101)

#htons
import socket
socket.htons(0x0101)

#htonl
import socket
socket.htonl(0xc0a80101)

#getaddrinfo
import socket
socket.getaddrinfo('www.google.com', 80, socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

#gethostbyname
import socket
