import socket
socket.if_indextoname(socket.if_nametoindex('en0'))

# The following code will show the IP address of your local ethernet adapter:

import socket
socket.gethostbyname(socket.gethostname())

# Get Local IP address of a machine:

import socket
socket.gethostbyname(socket.gethostname())

# DNS Lookup and reverse lookup:

import socket
socket.gethostbyaddr('208.67.222.222')
socket.gethostbyname('www.python.org')

# Socket Information:

import socket
hostname = 'google.com'
addr = socket.gethostbyname(hostname)
print ('The IP address of {} is {}'.format(hostname, addr))

# Get local IP address, not 127.0.0.1:

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print (s.getsockname()[0])
s.close()

# JSON Dumps:
