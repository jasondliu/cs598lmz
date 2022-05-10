import socket
socket.if_indextoname('3')

socket.gethostbyname('www.python.org')
socket.gethostbyaddr('216.58.192.142')

import urllib.request
u = urllib.request.urlopen('http://www.python.org')
u.read(200).decode('utf-8')

import urllib.request
req = urllib.request.Request('http://www.python.org',
                             data=b'This data is passed to stdin of the CGI')
f = urllib.request.urlopen(req)
f.read(100).decode('utf-8')

import urllib.request
req = urllib.request.Request('http://www.python.org',
                             data=b'This data is passed to stdin of the CGI',
                             headers={'Content-Type': 'text/plain'})
f = urllib.request.urlopen(req)
f.read(100).decode('utf-8')

import urllib.request
req = urllib.request.Request
