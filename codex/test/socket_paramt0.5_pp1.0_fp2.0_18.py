import socket
socket.if_indextoname(3)

import socket
socket.gethostname()

import socket
socket.gethostbyaddr('127.0.0.1')

import socket
socket.gethostbyname('www.baidu.com')

import socket
socket.getservbyname('ssh')

import socket
socket.getservbyport(80)

import socket
socket.getaddrinfo('www.baidu.com','http')

import socket
socket.getaddrinfo('www.baidu.com','http',socket.AF_INET)

import socket
socket.getaddrinfo('www.baidu.com','http',socket.AF_INET,socket.SOCK_STREAM)

import socket
socket.getaddrinfo('www.baidu.com','http',socket.AF_INET,socket.SOCK_STREAM,0,0)

import socket
socket.getaddrinfo('www.baidu.com','http',socket.AF_INET,socket.SOCK_STREAM,0,socket.AI_CANONNAME)

