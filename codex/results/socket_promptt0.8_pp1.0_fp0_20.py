import socket
# Test socket.if_indextoname
print socket.if_indextoname(1)

import _httpy
# Test _httpy.sendall()
s = _httpy.socket(socket.AF_INET, socket.SOCK_STREAM)
s.sendall("hi!")

# Test httpy.HTTPConnection.getresponse()
c = httplib.HTTPConnection('example.com')
c.connect()
r = c.getresponse()
r.read()
c.close()

# Test httpy.HTTPSConnection.getresponse()
c = httplib.HTTPSConnection('example.com')
c.connect()
r = c.getresponse()
r.read()
c.close()

# Test httplib.HTTPConnection.request() + httplib.HTTPConnection.getresponse()
c = httplib.HTTPConnection('example.com')
c.request('GET', '/')
r = c.getresponse()
r.read()
c.close()

# Test httplib.HTTPSConnection.request() + httplib.HTTPConnection.getresponse()

