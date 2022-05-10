import select
# Test select.select
print select.select([], [], [], 1) # blocking
print select.select([], [], [], 0) # non-blocking

import socket
# Test socket.getaddrinfo
print socket.getaddrinfo('www.google.com', 80)

import ssl
# Test ssl.wrap_socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.google.com', 443))
ssl_s = ssl.wrap_socket(s)
print ssl_s.write('GET / HTTP/1.0\r\n\r\n')
print ssl_s.read()
