import socket
socket.if_indextoname(3)

import socket
socket.gethostbyaddr('127.0.0.1')

import socket
socket.getaddrinfo('127.0.0.1', 80)

import socket
socket.getaddrinfo('127.0.0.1', 80, socket.AF_INET, socket.SOCK_STREAM)

import socket
socket.getaddrinfo('127.0.0.1', 80, socket.AF_INET, socket.SOCK_STREAM, 0, socket.AI_PASSIVE)

import socket
socket.getaddrinfo('127.0.0.1', 80, socket.AF_INET, socket.SOCK_STREAM, 0, socket.AI_PASSIVE, socket.AI_ADDRCONFIG)

import socket
socket.getaddrinfo('127.0.0.1', 80, socket.AF_INET, socket.SOCK_STREAM, 0, socket.AI_PASSIVE, socket.AI_ADDRCONFIG, socket.IPPROTO_TCP)

import socket
