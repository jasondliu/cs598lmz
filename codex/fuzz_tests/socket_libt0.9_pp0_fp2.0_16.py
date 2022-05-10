import socket

s = socket.socket()
port = 12345
s.bind(('', port))
s.listen(5)
print "Listening..."
while True:
	c, addr = s.accept()
	print 'Got connection from', addr
	c.close()
