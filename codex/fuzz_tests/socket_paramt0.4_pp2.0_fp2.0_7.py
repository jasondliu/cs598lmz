import socket
socket.if_indextoname(2)

socket.gethostbyname('localhost')
socket.gethostbyname_ex('localhost')

socket.gethostname()

socket.gethostbyaddr('127.0.0.1')

socket.getfqdn('127.0.0.1')

socket.getaddrinfo('localhost', 80, 0, 0, socket.IPPROTO_TCP)

import urllib.request
urllib.request.urlopen('http://www.python.org')

import urllib.request
req = urllib.request.Request('http://www.python.org')
req

urllib.request.urlopen(req)

import urllib.request
req = urllib.request.Request('http://www.python.org')
req.add_header('Referer', 'http://www.python.org/fish.html')
urllib.request.urlopen(req)

import urllib.request
req = urllib.request.Request('http://www.python.org')
req.add_header
